from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm

# Create your views here.

def index(request):
    pr = Property.objects.all()

    context = {
        'properties': pr
    }

    return render(request, 'properties/index.html', context)


def details_property(request, pk):
    property_details = Property.objects.get(id=pk)

    return render(request,'properties/property-details.html', {'property':property_details})


def create_property(request):
    form = PropertyForm()

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            propert = form.save(commit=False)
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'properties/form-template.html', context)