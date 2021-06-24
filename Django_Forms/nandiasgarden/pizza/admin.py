from django.contrib import admin

# Register your models here.
from .models import Size, Pizza

admin.site.register(Pizza)
admin.site.register(Size)