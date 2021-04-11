from rest_framework import serializers

from api.models import Job


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(read_only=True, source='company.name')

    class Meta:
        model = Job
        fields = ['id', 'created', 'company_id', 'title', 'is_active', 'location', 'description', 'skills', 'culture', 'company_name']
        read_only_fields = ['id', 'created', 'company_id']
