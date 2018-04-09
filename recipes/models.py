# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import User
from django.db import models


class IngredientType (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.title()


class Ingredient (models.Model):
    name = models.CharField(max_length=100)
    ingredientType = models.ForeignKey(
        IngredientType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.title() + " ( " + self.ingredientType.name.title() + " ) "


class Recipe (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField("Date Created", default=datetime.date.today)
    # CSV Steps for right now
    steps = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

    def stepsAsList(self):
        return [x.strip() for x in self.steps.split(',')]


class RecipeIngredient (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    oz = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.ingredient.name.title() + " " + self.ingredient.ingredientType.name.title() + "  - " + str(self.oz) + " oz "
