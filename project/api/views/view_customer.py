from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from api.models import Customer
from api.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            validate_email(email)
        except ValidationError:
            return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Customer.objects.filter(email=email).exists():
            return Response({'error': 'Customer with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        customer_id = kwargs.get('pk')
        if not Customer.objects.filter(id=customer_id).exists():
            return Response({'error': f'Customer not found {customer_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data.get('email')
        if email:
            try:
                validate_email(email)
            except ValidationError:
                return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
                 

        return super().update(request, *args, **kwargs)
    

    
    
    def destroy(self, request, *args, **kwargs):
        customer_id = kwargs.get('pk')
        if not Customer.objects.filter(id=customer_id).exists():
            return Response({'error': f'Customer not found {customer_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)      
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f'Customer {customer_id} has been deleted successfully'}, status=status.HTTP_200_OK)
