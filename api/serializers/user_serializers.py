from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_username', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio', 'finished_registration']
        read_only_fields = ['id', 'created']


class UserDetailSerializer(serializers.ModelSerializer):
    from .company_position_serializers.company_position_company_serializer import CompanyPositionCompanySerializer

    positions = CompanyPositionCompanySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_username', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio', 'positions', 'finished_registration']
        read_only_fields = ['id', 'created', 'positions']
