from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet

from api.models import Job
from api.serializers import JobSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if is_active := self.request.query_params.get('is_active'):
            if is_active == 'true':
                return queryset.filter(is_active=True)
            if is_active == 'false':
                return queryset.filter(is_active=False)
            raise ValidationError({'is_developer': "This field must be 'true' or 'false'."})

        return queryset

    def get_serializer_class(self):
        if self.action != 'retrieve':
            return JobSerializer
        return JobDetailSerializer


# class JobDetailSerializer(serializers.ModelSerializer):
    # future implementation of JobDetailSerializer
