from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from api.models import TaskBoard, Employee
from api.serializers import TaskBoardSerializer

class TaskBoardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskBoardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  
    search_fields = ['title', 'description']

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        if not title:
            return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        assigned_to_id = request.data.get('assigned_to')
        if assigned_to_id and not Employee.objects.filter(id=assigned_to_id).exists():
            return Response({'error': f'Employee not found {assigned_to_id}'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            search_query = self.request.query_params.get('search', None)
            if search_query:
                search_terms = search_query.strip('"')
                for term in search_terms.split():
                    page = [item for item in page if term.lower() in item.title.lower() or term.lower() in item.description.lower()]
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        taskboard_id = kwargs.get('pk')
        if not TaskBoard.objects.filter(id=taskboard_id).exists():
            return Response({'error': f'TaskBoard not found {taskboard_id}'}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        taskboard_id = kwargs.get('pk')
        if not TaskBoard.objects.filter(id=taskboard_id).exists():
            return Response({'error': f'TaskBoard not found {taskboard_id}'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f'TaskBoard {taskboard_id} has been deleted successfully'}, status=status.HTTP_200_OK)