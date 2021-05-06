from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Q

from .base_model import BaseModel


class User(BaseModel, AbstractBaseUser):
    name = models.TextField()
    email = models.EmailField(unique=True)
    auth0_id = models.TextField(unique=True)
    linkedin_username = models.TextField(blank=True, default='')
    github_username = models.TextField(blank=True, default='')
    is_developer = models.BooleanField(default=False)
    location = models.TextField()
    avatar_url = models.URLField(blank=True, default='')
    languages = ArrayField(base_field=models.TextField(), default=list, blank=True)
    skills = ArrayField(base_field=models.TextField(), default=list, blank=True)
    bio = models.TextField(blank=True, default='')
    finished_registration = models.BooleanField(default=False)

    USERNAME_FIELD = 'auth0_id'
    EMAIL_FIELD = 'email'
    password = None
    last_login = None

    objects = UserManager()

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(is_developer=False) | (Q(is_developer=True) & ~Q(github_username__exact='')),
                                   name='required_developer_fields'),
            models.UniqueConstraint(fields=['linkedin_username'],
                                    condition=~Q(linkedin_username__exact=''),
                                    name='unique_linkedin_username'),
            models.UniqueConstraint(fields=['github_username'],
                                    condition=~Q(github_username__exact=''),
                                    name='unique_github_username'),
        ]
