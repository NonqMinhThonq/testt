from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Product, User
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if not name:
            return Response({'error': 'Name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Product.objects.filter(name=name).exists():
            return Response({'error': 'Product with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        created_by_id = self.request.data.get('created_by')
        if created_by_id:
            user = User.objects.get(id=created_by_id)
            serializer.save(created_by=user)
        else:
            serializer.save()

    def update(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        if not Product.objects.filter(id=product_id).exists():
            return Response({'error': f'Product not found {product_id}'}, status=status.HTTP_400_BAD_REQUEST)      
        
        return super().update(request, *args, **kwargs)

    
    def destroy(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        if not Product.objects.filter(id=product_id).exists():
            return Response({'error': f'Product not found {product_id}'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f'Product {product_id} has been deleted successfully'}, status=status.HTTP_200_OK)
