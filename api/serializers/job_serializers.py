from rest_framework import serializers

from api.models import Job


class JobSerializer(serializers.ModelSerializer):
    company_id = serializers.CharField(read_only=True, source='company.id')
    company_name = serializers.CharField(read_only=True, source='company.name')
    company_slogan = serializers.CharField(read_only=True, source='company.slogan')
    company_location = serializers.CharField(read_only=True, source='company.location')
    logo_url = serializers.CharField(read_only=True, source='company.logo_url')

    class Meta:
        model = Job
        fields = ['id', 'created', 'company_id', 'title', 'is_active', 'location', 'description', 'languages', 'skills',
                  'cultures', 'company_name', 'company_slogan', 'company_location', 'logo_url']
        read_only_fields = ['id', 'created', 'company_id', 'company_name', 'company_slogan', 'company_location', 'logo_url']