from django.contrib import admin
from .models import DataStore

models_list = [DataStore]
admin.site.register(models_list)