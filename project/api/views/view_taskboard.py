from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import TaskBoard, Employee
from api.serializers import TaskBoardSerializer

class TaskBoardViewSet(viewsets.ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer
    permission_classes = [IsAuthenticated]

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