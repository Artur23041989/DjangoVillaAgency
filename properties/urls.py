from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details-property/<str:pk>/', views.details_property, name='details_property'),
    path('all-properties/', views.all_properties, name='all_properties'),
    path('about/', views.about, name='about'),
    path('add-review/', views.add_review, name='add_review'),
]
