from rest_framework import serializers

from api.models import CompanyPosition, Company, User


class CompanyPositionSerializer(serializers.ModelSerializer):
    from ..company_serializers import CompanySerializer
    from ..user_serializers import UserSerializer

    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True, source='company')
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')

    class Meta:
        model = CompanyPosition
        fields = ['id', 'created', 'company', 'company_id', 'user', 'user_id', 'is_admin', 'can_edit',
                  'can_create_jobs', 'title', 'description', 'start_date', 'end_date', 'activated']
        read_only_fields = ['id', 'created', 'company', 'user']
