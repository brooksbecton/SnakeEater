from django.db import models
from recipes.models import Ingredient

# Create your models here.
class UserIngredient (models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE)
    oz = models.FloatField(null=True, blank=True)
