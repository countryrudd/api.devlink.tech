from django.db import models

from .base_model import BaseModel
from .company_position import CompanyPosition


class Company(BaseModel):
    name = models.TextField()
    location = models.TextField()
    email = models.EmailField()
    slogan = models.TextField(blank=True, default='')
    logo_url = models.URLField(blank=True, default='')

    def current_positions(self):
        return CompanyPosition.objects.filter(company=self, end_date__isnull=True)
