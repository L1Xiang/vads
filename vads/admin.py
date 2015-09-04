from django.contrib import admin
from vads.models import Screen
from vads import models

# Register your models here.
admin.site.register(Screen)
admin.site.register(models.Ad)