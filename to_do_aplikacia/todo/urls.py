from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('del/<int:item_id>/', views.remove, name='remove_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('sort_by_date/', views.index, name='sort_by_date'),
]