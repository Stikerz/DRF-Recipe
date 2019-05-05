from rest_framework.serializers import ModelSerializer

from .models import Step, Ingredient, Recipe

from django.contrib.auth import get_user_model



class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('text',)


class StepSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = ('step_text',)


class RecipeSerializer(ModelSerializer):
    recipe_ingredients = IngredientSerializer(many=True)
    recipe_steps = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('name', 'recipe_ingredients', 'recipe_steps')

    def create(self, validated_data):
        recipe_ingredients: list = validated_data.pop('recipe_ingredients')
        recipe_steps: list = validated_data.pop('recipe_steps')
        user = validated_data.pop('user')
        recipe_instance, created = Recipe.objects.get_or_create(
            user=user,
                                                **validated_data)
        for ingrediants in recipe_ingredients:
            Ingredient.objects.create(recipe=recipe_instance, **ingrediants)
        for step in recipe_steps:
            Step.objects.create(recipe=recipe_instance, **step)
        return recipe_instance

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()

        recipe_ingredients = validated_data['recipe_ingredients']
        recipe_steps = validated_data['recipe_steps']

        ingredient = instance.recipe_ingredients.all()
        ingredient.delete()

        step = instance.recipe_steps.all()
        step.delete()

        for ingrediants in recipe_ingredients:
            Ingredient.objects.get_or_create(recipe=instance, **ingrediants)
        for step in recipe_steps:
            Step.objects.create(recipe=instance, **step)
            
        return instance
