from django.contrib import admin
from .models import Journal, Author, Category

admin.site.register(Author)
admin.site.register(Journal)
admin.site.register(Category)
