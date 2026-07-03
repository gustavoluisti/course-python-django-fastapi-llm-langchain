from django.contrib import admin
from business import models

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('social_name', 'cnpj', 'is_active', 'created_at', 'updated_at')
    search_fields = ('social_name', 'cnpj',)
    list_filter = ('is_active',)

admin.site.register(models.Business, BusinessAdmin)

