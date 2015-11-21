from django.db import models

# Create your models here.

# Represents a single drink to be used for a recipe.
class Drink(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    total_available = models.IntegerField()

# Represents an ingredient for a particular recipe.
class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe', related_name='ingredients')
    name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.IntegerField()

# Recipe model definition for SQL schema creation.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, blank=True, default='')
    recipe_description = models.CharField(max_length=100, blank=True, default='')
    #ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', default='')
    owner = models.ForeignKey('auth.User', related_name='recipe_set', default='')

# Recipe Instruction command.
class RecipeInstruction(models.Model):
    pump_a = models.DecimalField(decimal_places = 1, max_digits =2)
    pump_b = models.DecimalField(decimal_places = 1, max_digits =2)
    pump_c = models.DecimalField(decimal_places = 1, max_digits =2)
    pump_d = models.DecimalField(decimal_places = 1, max_digits =2)
    pump_e = models.DecimalField(decimal_places = 1, max_digits =2)
    pump_f = models.DecimalField(decimal_places = 1, max_digits =2)
    num_parallel = models.IntegerField()
