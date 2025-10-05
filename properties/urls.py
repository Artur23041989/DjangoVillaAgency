from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details_property/<str:pk>/', views.details_property, name='details-property'),
    path('create_property/<str:pk>/', views.create_property, name='create-property'),

]
