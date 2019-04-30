from django.urls import path

from .views import (RecipeListAPIView,
                    RecipeDetailAPIView,
                    CreateRecipeAPIView,
                    RecipeUpdateAPIView,
                    RecipeDestroyAPIView)

urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='recipe_list'),
    path('<int:pk>/', RecipeDetailAPIView.as_view(), name='recipe_detail'),
    path('create/', CreateRecipeAPIView.as_view(), name='recipe_create'),
    path('<int:pk>/update', RecipeUpdateAPIView.as_view(),
         name='recipe_update'),
    path('<int:pk>/delete', RecipeDestroyAPIView.as_view(),
         name='recipe_delete'),
]
