
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jameel, name='jameel'),
    path('routes/', views.routes, name='routes'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    
]