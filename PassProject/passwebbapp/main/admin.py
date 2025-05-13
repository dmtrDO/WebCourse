from django.contrib import admin
from . import models

admin.site.register(models.Roles)
admin.site.register(models.Settings)
admin.site.register(models.Users)
admin.site.register(models.GeneratedPasswords)




