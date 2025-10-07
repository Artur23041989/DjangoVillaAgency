from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details-property/<str:pk>/', views.details_property, name='details_property'),
    path('create-property/', views.create_property, name='create_property'),

]
