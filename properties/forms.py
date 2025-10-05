from django.forms import ModelForm
from .models import Property

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'category', 'description', 'price', 'image',
                  'bedrooms', 'bathrooms', 'area', 'floor', 'parking']