import operator
from functools import reduce

from django.db import transaction
from django.db.models import Q
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers import UserSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return PermissionDenied()

    def update(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super().update(request, *args, **kwargs)
        return PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object():
            return super().partial_update(request, *args, **kwargs)
        return PermissionDenied()

    @transaction.atomic()
    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object():
            for position in request.user.positions.all():
                # If the user being deleted is the company admin, delete the company.
                if position.is_admin:
                    for company_job in position.company.jobs.all():
                        company_job.delete()
                    for company_position in position.company.positions.all():
                        company_position.delete()
                    position.company.delete()
            return super().destroy(request, *args, **kwargs)
        return PermissionDenied()

    def get_object(self):
        if self.kwargs.get(self.lookup_url_kwarg or self.lookup_field) == 'current':
            if self.request.user is not None and isinstance(self.request.user, User):
                self.kwargs[self.lookup_field] = self.request.user.id
            else:
                raise PermissionDenied()
        return super().get_object()

    def get_queryset(self):
        queryset = super().get_queryset()

        if is_developer := self.request.query_params.get('is_developer'):
            if is_developer == 'true':
                queryset = queryset.filter(is_developer=True)
            elif is_developer == 'false':
                queryset = queryset.filter(is_developer=False)
            else:
                raise ValidationError({'is_developer': "This field must be 'true' or 'false'."})

        filter_kwargs = {}

        if linkedin_username := self.request.query_params.get('linkedin_username'):
            filter_kwargs['linkedin_username__exact'] = linkedin_username

        if github_username := self.request.query_params.get('github_username'):
            filter_kwargs['github_username__exact'] = github_username

        if search := self.request.query_params.get('search'):
            filter_kwargs['name__icontains'] = search
            filter_kwargs['email__icontains'] = search

            if is_developer:
                filter_kwargs['github_username__icontains'] = search

        if languages := self.request.query_params.getlist('language'):
            filter_kwargs['languages__overlap'] = languages

        if skills := self.request.query_params.getlist('skill'):
            filter_kwargs['skills__overlap'] = skills

        if locations := self.request.query_params.getlist('location'):
            filter_kwargs['location__in'] = locations

        if filter_kwargs:
            return queryset.filter(reduce(operator.or_, [Q(**{key: filter_kwargs[key]}) for key in filter_kwargs]))

        return queryset

    def get_serializer_class(self):
        if self.action != 'retrieve':
            return UserSerializer
        return UserDetailSerializer
