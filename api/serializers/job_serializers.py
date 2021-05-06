from rest_framework import serializers

from api.models import Job, Company


class JobSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company')
    company_name = serializers.CharField(read_only=True, source='company.name')
    company_slogan = serializers.CharField(read_only=True, source='company.slogan')
    company_location = serializers.CharField(read_only=True, source='company.location')
    logo_url = serializers.CharField(read_only=True, source='company.logo_url')
    email = serializers.EmailField(read_only=True, source='company.email')

    class Meta:
        model = Job
        fields = ['id', 'created', 'company_id', 'title', 'is_active', 'location', 'description', 'languages', 'skills',
                  'cultures', 'company_name', 'company_slogan', 'company_location', 'logo_url', 'email']
        read_only_fields = ['id', 'created', 'company_name', 'company_slogan', 'company_location',
                            'logo_url', 'email']
