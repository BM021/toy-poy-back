from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Card)
admin.site.register(models.Star)
admin.site.register(models.Shop)
admin.site.register(models.DutyArtist)
admin.site.register(models.Leading)
admin.site.register(models.Other)
admin.site.register(models.Ad)
admin.site.register(models.AdCatalog)
