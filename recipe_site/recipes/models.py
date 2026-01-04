from django.db import models
from django.contrib.auth.models import User


# Категория рецепта (например: Завтрак, Обед)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Рецепт
class Recipe(models.Model):
    title = models.CharField(max_length=200)  # название рецепта
    description = models.TextField()          # описание
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


# Комментарий к рецепту
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]


# Оценка рецепта (1–5)
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    value = models.IntegerField()