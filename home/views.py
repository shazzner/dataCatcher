from django.shortcuts import render

# Create your views here.
def listings(request):
    return render(request, 'home/listings.html')

def index(request):
    return render(request, 'home/index.html')

