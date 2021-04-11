from django.contrib.postgres.fields import ArrayField
from django.db import models

from .base_model import BaseModel


class Job(BaseModel):
    title = models.TextField()
    location = models.TextField()
    description = models.TextField(blank=True, default='')
    skills = ArrayField(base_field=models.TextField())
    culture = ArrayField(base_field=models.TextField())
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey('Company', related_name='jobs', on_delete=models.CASCADE)