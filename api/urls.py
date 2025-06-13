# urls.py

from django.urls import path
from .views import user_list, user_create, user_login, expense_list_create, expense_update_delete, user_delete


urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('user/create/', user_create, name='user-create'), 
    path('user/login/', user_login, name='user-login'),
    path('expenses/', expense_list_create, name='expense-list-create'),
    path('expenses/<int:pk>/', expense_update_delete, name='expense-update-delete'),
    path('user/delete/<int:pk>/', user_delete, name='user-delete'),
]