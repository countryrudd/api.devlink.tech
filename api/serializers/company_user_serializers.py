from rest_framework import serializers

from api.models import CompanyUser


class CompanyUserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True, source='user.name')
    email = serializers.EmailField(read_only=True, source='user.email')
    location = serializers.CharField(read_only=True, source='user.location')
    avatar_url = serializers.URLField(read_only=True, source='user.location')

    class Meta:
        model = CompanyUser
        fields = ['id', 'created', 'name', 'email', 'location', 'avatar_url']
        read_only_fields = ['id', 'created', 'name', 'email', 'location', 'avatar_url']
