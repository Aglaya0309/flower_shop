from django.contrib import admin
from .models import Flower  # Импортируем модель

admin.site.register(Flower)  # Регистрируем её

