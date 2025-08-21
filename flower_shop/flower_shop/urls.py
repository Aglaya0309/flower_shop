from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # Главная и каталог
    path('accounts/', include('accounts.urls')),  # Регистрация/авторизация
    path('orders/', include('orders.urls')),  # Корзина и заказы
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
