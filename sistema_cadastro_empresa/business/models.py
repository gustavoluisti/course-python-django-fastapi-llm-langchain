import uuid
from django.db import models

class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    social_name = models.CharField(max_length=500)
    cnpj = models.CharField(max_length=14)
    is_active = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address_street = models.CharField(max_length=200, null=True, blank=True)
    address_number = models.CharField(max_length=10, null=True, blank=True)
    address_neighborhood = models.CharField(max_length=100, null=True, blank=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_state = models.CharField(max_length=2, null=True, blank=True)
    address_zip_code = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'businesses'

    def __str__(self):
        return self.social_name