from django.contrib import admin
from . import models
from .models import Author, Category, Post , Comments

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comments)



