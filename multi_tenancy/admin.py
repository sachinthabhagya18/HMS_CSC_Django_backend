from django.contrib import admin
from . import models

admin.site.register(models.Tenant)
admin.site.register(models.TenantUser)
