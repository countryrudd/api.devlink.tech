from rest_framework import serializers

from api.models import CompanyPosition


class CompanyPositionSerializer(serializers.ModelSerializer):
    from .company_serializers import CompanySerializer
    from .user_serializers import UserSerializer

    user = UserSerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyPosition
        fields = ['id', 'created', 'user', 'company', 'is_admin', 'can_edit', 'can_create_jobs', 'title']
        read_only_fields = ['id', 'created', 'user', 'company']
