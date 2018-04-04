# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import User
from django.db import models


class Recipe (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField("Date Created", default=datetime.date.today)
    # CSV Steps for right now
    steps = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def stepsAsList(self):
        return [x.strip() for x in self.steps.split(',')]


class IngredientType (models.Model):
    name = models.CharField(max_length=100)


class Ingredient (models.Model):
    name = models.CharField(max_length=100)
    ingredientType = models.ForeignKey(
        IngredientType, on_delete=models.CASCADE)


class RecipeIngredient (models.Model):
    recipeId = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredientId = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    oz = models.IntegerField()
