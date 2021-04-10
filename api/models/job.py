from django.contrib.postgres.fields import ArrayField
from django.db import models

from api.models.base_model import BaseModel


class Job(BaseModel):
    title = models.TextField()
    location = models.TextField()
    description = models.TextField()
    skills = ArrayField(base_field=models.TextField())
    company = models.ForeignKey('Company', related_name='jobs', on_delete=models.CASCADE)
