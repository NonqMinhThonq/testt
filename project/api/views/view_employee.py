from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from api.models import Employee
from api.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Employee.objects.filter(email=email).exists():
            return Response({'error': 'Employee with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': f'Employee not found {employee_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data.get('email')
        if email:
            try:
                validate_email(email)
            except ValidationError:
                return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().update(request, *args, **kwargs)

    
    def destroy(self, request, *args, **kwargs):
        employee_id = kwargs.get('pk')
        if not Employee.objects.filter(id=employee_id).exists():
            return Response({'error': f'Employee not found {employee_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f'Employee {employee_id} has been deleted successfully'}, status=status.HTTP_200_OK)