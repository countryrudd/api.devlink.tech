from django.db import transaction
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from api.models import CompanyPosition
from api.serializers.company_position_serializers.company_position_serializer import CompanyPositionSerializer


class CompanyPositionViewSet(ModelViewSet):
    queryset = CompanyPosition.objects.all()
    serializer_class = CompanyPositionSerializer
    http_method_names = ['post', 'patch', 'delete', 'head']

    def list(self, request, *args, **kwargs):
        return PermissionDenied()

    def retrieve(self, request, *args, **kwargs):
        return PermissionDenied()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user:
            position = self.get_object()
            if user_position := CompanyPosition.objects.filter(company=position.company, user=request.user).first():
                if user_position.is_admin:
                    return super().update(request, *args, **kwargs)
        raise PermissionDenied()

    @transaction.atomic()
    def partial_update(self, request, *args, **kwargs):
        if request.user:
            position = self.get_object()
            if user_position := CompanyPosition.objects.filter(company=position.company, user=request.user).first():
                if user_position.is_admin:
                    return super().partial_update(request, *args, **kwargs)
        raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user:
            position = self.get_object()
            if user_position := CompanyPosition.objects.filter(company=position.company, user=request.user).first():
                if user_position.is_admin:
                    return super().destroy(request, *args, **kwargs)
        raise PermissionDenied()
