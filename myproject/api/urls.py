from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('<int:id>/', views.getItemById), 
    path('delete/<int:id>/', views.deleteItemById),
]