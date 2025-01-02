
from django.contrib import admin
from api.models import Customer, Product, Employee, TaskBoard

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'has_purchased', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('has_purchased', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'created_by')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'created_by')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'position', 'department', 'company')
    search_fields = ('full_name', 'email', 'phone', 'position', 'department', 'company')
    list_filter = ('department', 'company')

@admin.register(TaskBoard)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to', 'due_date', 'created_at', 'created_by')
    search_fields = ('title', 'description')
    list_filter = ('status', 'assigned_to', 'due_date', 'created_at', 'created_by')