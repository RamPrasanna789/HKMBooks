from django.shortcuts import redirect, render
from store.models import Product

def home(request):
    proudcts = Product.objects.all().filter(is_available=True)
    context = {
        'products': proudcts
    }
    return render(request, 'home.html', context)