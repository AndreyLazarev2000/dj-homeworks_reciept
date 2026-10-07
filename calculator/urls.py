from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),          # ← главная
    path('<str:recipe_name>/', views.recipe_view, name='recipe'),
]