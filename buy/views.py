from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, Product, Produce
import datetime as dt

# Create your views here.
def index(request):
    date = dt.date.today()
    image = Image.objects.all()
    product = Product.objects.all()
    produce = Produce.objects.all()
    
    return render(request, 'index.html', {"date": date, "image":image, "product": product, "produce": produce})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})
