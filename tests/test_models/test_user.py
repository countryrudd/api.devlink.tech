import pytest
from django.db import IntegrityError

from api.models import User


@pytest.mark.django_db
class TestUser:
    @pytest.mark.django_db(transaction=True)
    def test_create_duplicate_github_username(self):
        User.objects.create(name='Test User', email='test@test.com', auth0_id='auth|12345', linkedin_id='12345',
                            github_username='test', is_developer=True, location='Charlotte, NC', avatar_url='',
                            languages=['English'], skills=['Python'])
        with pytest.raises(IntegrityError):
            User.objects.create(name='Test User', email='test@test.com', auth0_id='auth|12345', linkedin_id='12345',
                                github_username='test', is_developer=True, location='Charlotte, NC', avatar_url='',
                                languages=['English'], skills=['Python'])
        assert User.objects.count() == 1

    @pytest.mark.django_db(transaction=True)
    def test_create_developer_without_github_username(self):
        with pytest.raises(IntegrityError):
            User.objects.create(name='Test User', email='test@test.com', auth0_id='auth|12345', linkedin_id='12345',
                                github_username='', is_developer=True, location='Charlotte, NC', avatar_url='',
                                languages=['English'], skills=['Python'])
        assert User.objects.count() == 0
