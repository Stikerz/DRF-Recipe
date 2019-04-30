from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False)


class Ingredient(models.Model):
    text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='recipe_ingredients')


class Step(models.Model):
    step_text = models.TextField(null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='recipe_steps')