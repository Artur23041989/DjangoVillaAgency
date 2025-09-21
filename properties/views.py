from django.shortcuts import render
from .models import Properties

# Create your views here.

def index(request):
    pr = Properties.objects.all()

    context = {
        'properties': pr
    }

    return render(request, 'properties/index.html', context)