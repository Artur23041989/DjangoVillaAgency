from django.shortcuts import render, redirect
from .models import Property
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.

def index(request):
    pr = Property.objects.all()

    context = {
        'properties': pr
    }
    return render(request, 'properties/index.html', context)


def all_properties(request):
    pr = Property.objects.all()
    page = request.GET.get('page')
    results = 1
    paginator = Paginator(pr, results)

    try:
        pr = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        pr = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        pr = paginator.page(page)

    left_index = int(page) - 4

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
        'properties': pr,
        "paginator": paginator,
        "custom_range": custom_range
    }
    return render(request, 'properties/all_properties.html', context)


def details_property(request, pk):
    property_details = Property.objects.get(id=pk)

    return render(request,'properties/property-details.html', {'property':property_details})

def about(request):
    return render(request, 'properties/about.html')



def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')  # Название страницы с отзывами
    else:
        form = ReviewForm()
    return render(request, 'properties/add_review.html', {'form': form})



def reviews_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'properties/about.html', {'reviews': reviews})


