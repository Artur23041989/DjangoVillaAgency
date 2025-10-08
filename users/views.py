from django.shortcuts import render

def profiles(request):
    return render(request, 'users/agent_card.html')

# Create your views here.
