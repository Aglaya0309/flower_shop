from django.shortcuts import render
from .models import Flower

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'products/flower_list.html', {'flowers': flowers})