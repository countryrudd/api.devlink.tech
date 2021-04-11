from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio']
        read_only_fields = ['id', 'created']


class UserDetailSerializer(serializers.ModelSerializer):
    from .company_position_serializers.company_position_company_serializer import CompanyPositionCompanySerializer

    positions = CompanyPositionCompanySerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio', 'positions']
        read_only_fields = ['id', 'created', 'positions']
