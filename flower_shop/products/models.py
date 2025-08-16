from django.db import models

class Flower(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    image = models.ImageField("Изображение", upload_to='flowers/')
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Цветок"
        verbose_name_plural = "Цветы"

    def __str__(self):
        return self.name