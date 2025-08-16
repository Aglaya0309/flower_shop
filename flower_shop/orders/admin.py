from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  # Встроенное отображение товаров в заказе
    model = OrderItem
    extra = 0  # Убираем пустые поля для новых товаров

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'delivery_address']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'delivery_address']  # Поиск по имени пользователя/адресу
    inlines = [OrderItemInline]  # Добавляем вложенные товары

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'flower', 'quantity']
    list_select_related = ['order', 'flower']  # Оптимизация запросов к БД