from django.shortcuts import render
from .models import Property

# Create your views here.

def index(request):
    pr = Property.objects.all()

    context = {
        'properties': pr
    }

    return render(request, 'properties/index.html', context)