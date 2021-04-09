from rest_framework import serializers

from api.models import CompanyUserPermissions


class CompanyUserPermissionsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True, source='user.name')
    email = serializers.EmailField(read_only=True, source='user.email')
    location = serializers.CharField(read_only=True, source='user.location')
    avatar_url = serializers.URLField(read_only=True, source='user.location')

    class Meta:
        model = CompanyUserPermissions
        fields = ['id', 'created', 'name', 'email', 'location', 'avatar_url', 'is_admin', 'can_edit', 'can_create_jobs']
        read_only_fields = ['id', 'created', 'name', 'email', 'location', 'avatar_url']
