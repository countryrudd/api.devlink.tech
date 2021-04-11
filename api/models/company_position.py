from django.db import models

from .base_model import BaseModel


class CompanyPosition(BaseModel):
    company = models.ForeignKey('Company', related_name='positions', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='positions', on_delete=models.CASCADE)
    title = models.TextField()
    is_admin = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_create_jobs = models.BooleanField(default=False)
