import operator
from functools import reduce

from django.db.models import Q
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet

from api.models import Job, CompanyPosition
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
        if request.user:
            if not (company_id := request.data['company_id']):
                raise ValidationError({'company_id': 'This field is required.'})
            if company_position := CompanyPosition.objects.filter(user=request.user, company_id=company_id).first():
                if company_position.can_create_jobs:
                    return super().create(request, *args, **kwargs)
        raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        if request.user:
            job = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=job.company, user=request.user).first():
                if company_position.can_create_jobs:
                    return super().update(request, *args, **kwargs)
        raise PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        if request.user:
            job = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=job.company, user=request.user).first():
                if company_position.can_create_jobs:
                    return super().partial_update(request, *args, **kwargs)
        raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        if request.user:
            job = self.get_object()
            if company_position := CompanyPosition.objects.filter(company=job.company, user=request.user).first():
                if company_position.can_create_jobs:
                    return super().destroy(request, *args, **kwargs)
        raise PermissionDenied()

    def get_queryset(self):
        queryset = super().get_queryset()

        if is_active := self.request.query_params.get('is_active'):
            if is_active == 'true':
                queryset = queryset.filter(is_active=True)
            elif is_active == 'false':
                queryset = queryset.filter(is_active=False)
            else:
                raise ValidationError({'is_active': "This field must be 'true' or 'false'."})

        filter_kwargs = {}

        if search := self.request.query_params.get('search'):
            filter_kwargs['title__icontains'] = search

        if languages := self.request.query_params.getlist('language'):
            filter_kwargs['languages__overlap'] = languages

        if skills := self.request.query_params.getlist('skill'):
            filter_kwargs['skills__overlap'] = skills

        if locations := self.request.query_params.getlist('location'):
            filter_kwargs['location__in'] = locations

        if cultures := self.request.query_params.getlist('culture'):
            filter_kwargs['cultures__overlap'] = cultures

        if filter_kwargs:
            return queryset.filter(reduce(operator.or_, [Q(**{key: filter_kwargs[key]}) for key in filter_kwargs]))

        return queryset

    def get_serializer_class(self):
        return JobSerializer
