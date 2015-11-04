from rest_framework import serializers
from django.contrib.auth.models import User
from minimixer_manager.models import Recipe, RecipeIngredient, Ingredient, RecipeInstruction

# Serializer used to turn Main User account JSON requests into Python datatypes
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# Serializer used to turn Main User account authentication requests into Python datatypes
class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_description','ingredients', 'owner')

class RecipeInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeInstruction
        fields = ('pump_a', 'pump_b', 'pump_c', 'pump_d', 'pump_e', 'pump_f', 'num_parallel')
