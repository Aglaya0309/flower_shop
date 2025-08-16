from django.db import models
from accounts.models import CustomUser
from products.models import Flower

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)