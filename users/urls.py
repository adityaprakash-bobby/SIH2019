from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('profile/', views.profile, name='user-profile')
]