# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Recipe, RecipeIngredient


class IndexView(generic.ListView):
    template_name = 'recipes/index.html'

    def get_queryset(self):
        """Return the last five published recipes."""
        return Recipe.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class NewRecipeView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ['name', 'description', 'steps']
    success_url = '/recipes'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(generic.CreateView, self).form_valid(form)


class UpdateRecipeView(LoginRequiredMixin, generic.UpdateView):
    model = Recipe
    template_name = "recipes/update.html"
    fields = ['name', 'description', 'steps']
    success_url = '/recipes'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(generic.UpdateView, self).form_valid(form)


class DeleteRecipeView(LoginRequiredMixin, generic.DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = '/recipes'
