from django.http import HttpResponse
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    text = ""

    for recipe in recipes:
        text += recipe.title + "<br>"

    return HttpResponse(text)