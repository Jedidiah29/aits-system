from django.contrib import admin

# Register your models here.

from .models import Issue

admin.site.register(Issue)