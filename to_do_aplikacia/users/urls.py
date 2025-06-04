from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.sign_in, name='login'),
    path('sign_out/', views.sign_out, name='sign_out'),
]