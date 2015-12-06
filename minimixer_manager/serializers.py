from rest_framework import serializers
from django.contrib.auth.models import User
from minimixer_manager.models import Recipe, Drink, Ingredient, RecipeInstruction

# Serializer used to turn Main User account JSON requests into Python datatypes
class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')



# Serializer used to turn Main User account authentication requests into Python datatypes
class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

# Serializer for Recipe-specific ingredients
class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        #fields = ('recipe', 'name', 'quantity')

# Serializer used for creating recipes.
class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        #fields = ('recipe_name', 'recipe_description','ingredients', 'owner')

    #def create(self, validated_data):
    #    ingredients_data = validated_data.pop('ingredients')
    #    recipe = Recipe.objects.create(**validated_data)
    #    for ingredient_data in ingredients_data:
    #        Ingredient.objects.create(recipe=recipe, **ingredient_data)
    #    return recipe


# Serializer used for the possible recipe ingredients.
class DrinkSerializer(serializers.ModelSerializer):
    # Associated recipe ingredients with this drink.
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Drink
        #fields = ('name', 'description', 'total_available')


# Defines the data for an instruction to give to the uc.
class RecipeInstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeInstruction
        fields = ('pump_a', 'pump_b', 'pump_c', 'pump_d', 'pump_e', 'pump_f', 'num_parallel')
