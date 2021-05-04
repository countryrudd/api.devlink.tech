from rest_framework import serializers

from api.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'email']
        read_only_fields = ['id', 'created']


class CompanyDetailSerializer(serializers.ModelSerializer):
    from .job_serializers import JobSerializer
    from .company_position_serializers.company_position_user_serializer import CompanyPositionUserSerializer

    jobs = JobSerializer(many=True, read_only=True)
    positions = CompanyPositionUserSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'created', 'name', 'location', 'slogan', 'logo_url', 'jobs', 'positions', 'email']
        read_only_fields = ['id', 'created', 'jobs', 'positions']
