from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Q

from api.models.base_model import BaseModel


class User(BaseModel):
    name = models.TextField()
    email = models.EmailField()
    auth0_id = models.TextField()
    linkedin_id = models.TextField()
    github_username = models.TextField(blank=True, default='')
    is_developer = models.BooleanField(default=False)
    location = models.TextField()
    avatar_url = models.URLField(blank=True, default='')
    languages = ArrayField(base_field=models.TextField())
    skills = ArrayField(base_field=models.TextField())

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(is_developer=False) | (Q(is_developer=True) & ~Q(github_username__exact='')),
                                   name='required_developer_fields'),
            models.UniqueConstraint(fields=['github_username'],
                                    condition=~Q(github_username__exact=''),
                                    name='unique_github_username'),
        ]
