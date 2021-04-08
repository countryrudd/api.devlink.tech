from django.db import models

from api.models.base_model import BaseModel


class Company(BaseModel):
    name = models.TextField()
    location = models.TextField()
    slogan = models.TextField(blank=True, default='')
    logo_url = models.URLField(blank=True, default='')