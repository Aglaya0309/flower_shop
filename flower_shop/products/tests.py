from django.test import TestCase
from .models import Flower

class FlowerModelTest(TestCase):
    def test_flower_creation(self):
        flower = Flower.objects.create(name="Роза", price=10.99)
        self.assertEqual(flower.name, "Роза")
        self.assertEqual(flower.price, 10.99)