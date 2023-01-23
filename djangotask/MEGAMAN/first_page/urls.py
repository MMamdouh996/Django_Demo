from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='home'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('about/', views.about, name ='about'),
    path('product/', views.product, name ='product'),
    path('viewcar/<id>', views.singleCar, name ='viewcar'),
    path('deleteCar/<id>',views.deleteCar, name="deleteCar"),
    path('createCar',views.createCar, name="createCar"),
    path('editCar/<id>',views.editCar, name="editCar"), 
]
