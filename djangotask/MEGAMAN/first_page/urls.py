from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('about/', views.about, name ='about'),
    path('product/', views.product, name ='product'),
    
]
