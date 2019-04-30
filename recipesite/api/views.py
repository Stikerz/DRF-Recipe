from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView)

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Recipe
from .serializers import RecipeSerializer


# Create your views here.
# You need to create API’s :
# 1. To create a new recipe
# 2. get recipes by particular user
# 3. get all the recipes
# 4. update a recipe, delete a particular recipe


class RecipeListAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailAPIView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RecipeDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CreateRecipeAPIView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
