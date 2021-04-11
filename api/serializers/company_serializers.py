from rest_framework import serializers

from api.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url']
        read_only_fields = ['id', 'created']


class CompanyDetailSerializer(serializers.ModelSerializer):
    from .job_serializers import JobSerializer
    from .company_position_serializers import CompanyPositionSerializer

    jobs = JobSerializer(many=True, read_only=True)
    employees = CompanyPositionSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'jobs', 'positions']
        read_only_fields = ['id', 'created', 'jobs', 'positions']
