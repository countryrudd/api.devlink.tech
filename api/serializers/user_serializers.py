from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio']
        read_only_fields = ['id', 'created']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'created', 'name', 'email', 'auth0_id', 'linkedin_id', 'github_username', 'is_developer',
                  'location', 'avatar_url', 'languages', 'skills', 'bio']
        read_only_fields = ['id', 'created']
