import operator
from functools import reduce

from django.db import transaction
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
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

    def get_queryset(self):
        queryset = super().get_queryset()

        filter_kwargs = {}

        if search := self.request.query_params.get('search'):
            filter_kwargs['name__icontains'] = search

        if locations := self.request.query_params.getlist('location'):
            filter_kwargs['location__in'] = locations

        if filter_kwargs:
            return queryset.filter(reduce(operator.or_, [Q(**{key: filter_kwargs[key]}) for key in filter_kwargs]))

        return queryset

    def get_serializer_class(self):
        if self.action != 'retrieve':
            return CompanySerializer
        return CompanyDetailSerializer
