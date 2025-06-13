# admiin.py
 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Expense


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)
    
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-date',)
    raw_id_fields = ('user',)