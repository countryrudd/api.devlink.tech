from rest_framework import serializers

from api.models import CompanyPosition


class CompanyPositionCompanySerializer(serializers.ModelSerializer):
    from api.serializers.company_serializers import CompanySerializer

    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyPosition
        fields = ['id', 'created', 'company', 'user_id', 'is_admin', 'can_edit', 'can_create_jobs', 'title',
                  'description', 'start_date', 'end_date']
        read_only_fields = ['id', 'created', 'company', 'user_id']
