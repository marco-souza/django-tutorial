from django.contrib import admin
from .models import Pet, Coordinate, Photo

# Register your models here.
admin.site.register(Pet)
admin.site.register(Photo)
admin.site.register(Coordinate)
