from django.db import models
from django.conf import settings


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField(blank=True)  # Добавил blank=True

    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.orderitem_set.all())

    def __str__(self):
        return f"Заказ #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower = models.ForeignKey('products.Flower', on_delete=models.CASCADE)  # Используем строковую ссылку
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.flower.price * self.quantity

    def __str__(self):
        return f"{self.flower.name} x{self.quantity}"