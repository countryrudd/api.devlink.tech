from rest_framework import serializers

from api.models import CompanyPosition


class CompanyPositionUserSerializer(serializers.ModelSerializer):
    from api.serializers.user_serializers import UserSerializer

    user = UserSerializer(read_only=True)

    class Meta:
        model = CompanyPosition
        fields = ['id', 'created', 'user', 'company_id', 'is_admin', 'can_edit', 'can_create_jobs', 'title']
        read_only_fields = ['id', 'created', 'user', 'company_id']
