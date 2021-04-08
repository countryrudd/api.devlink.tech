from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills']
        read_only_fields = ['id', 'created']


class UserDetailSerializer(serializers.ModelSerializer):
    from .company_serializers import CompanySerializer

    company = CompanySerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'company']
        read_only_fields = ['id', 'created', 'company']
