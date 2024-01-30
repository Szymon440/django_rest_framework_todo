from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_tasks),
    path('addTask/', views.create_task),
    path('updateTask/<int:task_id>/', views.update_task),
    path('deleteTask/<int:task_id>/', views.delete_task),
]
