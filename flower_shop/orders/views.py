from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Flower

@login_required
def add_to_cart(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    order, created = Order.objects.get_or_create(user=request.user, status='pending')
    OrderItem.objects.create(order=order, flower=flower, quantity=1)
    return redirect('cart')

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status='pending').first()
    return render(request, 'orders/cart.html', {'order': order})