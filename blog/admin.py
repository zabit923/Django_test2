from django.contrib import admin
from . import models




admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post)
admin.site.register(models.Recipe)
admin.site.register(models.Comment)
