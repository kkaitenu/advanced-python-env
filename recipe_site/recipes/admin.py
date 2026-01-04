from django.contrib import admin
from .models import Recipe, Category, Comment, Rating

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)