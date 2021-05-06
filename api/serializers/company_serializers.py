from django.db import transaction
from rest_framework import serializers

from api.models import Company, CompanyPosition


class CompanySerializer(serializers.ModelSerializer):
    created_by_position_title = serializers.CharField(write_only=True)
    created_by_position_description = serializers.CharField(write_only=True, allow_blank=True)
    created_by_position_start_date = serializers.DateField(write_only=True)

    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'email', 'created_by_position_title',
                  'created_by_position_description', 'created_by_position_start_date']
        read_only_fields = ['id', 'created']

    @transaction.atomic()
    def create(self, validated_date):
        created_by_position = validated_date.pop('created_by_position_title')
        created_by_position_description = validated_date.pop('created_by_position_description')
        created_by_position_start_date = validated_date.pop('created_by_position_start_date')

        company = super().create(validated_date)
        CompanyPosition.objects.create(
            user=self.context['request'].user,
            company=company,
            title=created_by_position,
            description=created_by_position_description,
            start_date=created_by_position_start_date,
            end_date=None,
            activated=True,
            is_admin=True,
            can_edit=True,
            can_create_jobs=True,
        )
        return company


class CompanyDetailSerializer(serializers.ModelSerializer):
    from .job_serializers import JobSerializer
    from .company_position_serializers.company_position_user_serializer import CompanyPositionUserSerializer

    jobs = JobSerializer(many=True, read_only=True)
    positions = CompanyPositionUserSerializer(many=True, read_only=True, source='current_positions')

    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'jobs', 'positions', 'email']
        read_only_fields = ['id', 'created', 'jobs', 'positions']
