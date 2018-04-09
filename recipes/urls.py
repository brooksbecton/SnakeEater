from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.NewRecipeView.as_view(), name='new'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.UpdateRecipeView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteRecipeView.as_view(), name='delete'),
]
