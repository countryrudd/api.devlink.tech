from django.db import models

from .base_model import BaseModel


class Company(BaseModel):
    name = models.TextField()
    location = models.TextField()
    email = models.EmailField()
    slogan = models.TextField(blank=True, default='')
    logo_url = models.URLField(blank=True, default='')
