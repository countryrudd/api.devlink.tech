from rest_framework import serializers

from api.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url']
        read_only_fields = ['id', 'created']


class CompanyDetailSerializer(serializers.ModelSerializer):
    from .job_serializers import JobSerializer
    from .company_user_permissions_serializers import CompanyUserPermissionsSerializer

    jobs = JobSerializer(many=True, read_only=True)
    employees = CompanyUserPermissionsSerializer(many=True, read_only=True, source='company_user_permissions')

    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'jobs', 'employees']
        read_only_fields = ['id', 'created', 'jobs', 'employees']
