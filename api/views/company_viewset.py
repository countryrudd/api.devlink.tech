from django.db import transaction
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Company, CompanyPosition
from api.serializers import CompanySerializer, CompanyDetailSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user:
            company = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=company, user=request.user).first():
                if company_position.can_edit:
                    return super().update(request, *args, **kwargs)
        raise PermissionDenied()

    @transaction.atomic()
    def partial_update(self, request, *args, **kwargs):
        if request.user:
            company = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=company, user=request.user).first():
                if company_position.can_edit:
                    for job in company_position.company.jobs.all():
                        job.delete()
                    for position in company_position.company.positions.all():
                        position.delete()
                    return super().partial_update(request, *args, **kwargs)
        raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user:
            company = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=company, user=request.user).first():
                if company_position.is_admin:
                    return super().destroy(request, *args, **kwargs)
        raise PermissionDenied()

    def get_serializer_class(self):
        if self.action != 'retrieve':
            return CompanySerializer
        return CompanyDetailSerializer

    @action(detail=True, methods=['POST'])
    @transaction.atomic
    def create_position(self, request, *args, **kwargs):
        from api.serializers.company_position_serializers.company_position_serializer import CompanyPositionSerializer

        if not request.user.positions.filter(company=self.get_object()).first():
            serializer = CompanyPositionSerializer(data={
                **request.data,
                'user_id': str(request.user.id),
                'company_id': str(self.get_object().pk)
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        raise PermissionDenied()
