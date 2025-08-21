from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Flower


@login_required
def add_to_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    order, created = Order.objects.get_or_create(user=request.user, status='pending')

    # Проверяем, есть ли уже этот цветок в корзине
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        flower=flower,
        defaults={'quantity': 1}
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')


@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, status='pending').first()
    return render(request, 'orders/cart.html', {'order': order})