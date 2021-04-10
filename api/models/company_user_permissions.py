from django.db import models

from .base_model import BaseModel


class CompanyUserPermissions(BaseModel):
    company = models.ForeignKey('Company', related_name='company_user_permissions', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='company_user_permissions', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_create_jobs = models.BooleanField(default=False)
