from django.db import models

from api.models.base_model import BaseModel


class CompanyUser(BaseModel):
    company = models.ForeignKey('Company', related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='companies', on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_create_jobs = models.BooleanField(default=False)
