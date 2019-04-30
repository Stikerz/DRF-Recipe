from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.utils import json
from rest_framework import status

from .models import Recipe
from .serializers import RecipeSerializer

User = get_user_model()


class RecipeTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='savetheworld',
                                   first_name="Thanos",
                                   last_name="Tital")
        user.set_password('gamora')
        user.save()

        Recipe.objects.create(user=user, name='Gauntlet')

        self.recipe_data = {
            "name": "Finger Snapper",
            "recipe_ingredients": [
                {
                    "text": "Soul Stone"
                },

                {
                    "text": "Power Stone"
                }
            ],
            "recipe_steps": [
                {
                    "step_text": "Add Soul Stone"
                },

                {
                    "step_text": "Add Power Stone"
                }
            ]

        }

        self.invalid_recipe_data = {
            "name": "",
            "recipe_ingredients": [],
            "recipe_steps": []

        }

    def test_create_valid_recipe(self):
        user_login = self.client.login(username="savetheworld",
                                       password="gamora")
        self.assertTrue(user_login)
        response = self.client.post('/api/recipes/create/', data=json.dumps(
            self.recipe_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_recipe(self):
        user_login = self.client.login(username="savetheworld",
                                       password="gamora")
        self.assertTrue(user_login)
        response = self.client.post('/api/recipes/create/', data=json.dumps(
            self.invalid_recipe_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_recipe_list(self):
        user_login = self.client.login(username="savetheworld", password="gamora")
        self.assertTrue(user_login)
        response = self.client.get('/api/recipes/')
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_recipe(self):
        user_login = self.client.login(username="savetheworld", password="gamora")
        self.assertTrue(user_login)
        response = self.client.get('/api/recipes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_detail_recipe(self):
        user_login = self.client.login(username="savetheworld", password="gamora")
        self.assertTrue(user_login)
        response = self.client.get('/api/recipes/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_recipe(self):
        user_login = self.client.login(username="savetheworld",
                                       password="gamora")
        self.assertTrue(user_login)
        response = self.client.put('/api/recipes/1/update', data=json.dumps(
            self.recipe_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_recipe_invalid_data(self):
        user_login = self.client.login(username="savetheworld",
                                       password="gamora")
        self.assertTrue(user_login)
        response = self.client.put('/api/recipes/1/update', data=json.dumps(
            self.invalid_recipe_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_delete_recipe(self):
        user_login = self.client.login(username="savetheworld",
                                       password="gamora")
        self.assertTrue(user_login)
        response = self.client.delete('/api/recipes/1/delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

