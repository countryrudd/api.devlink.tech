from rest_framework.exceptions import ValidationError
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
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if is_developer := self.request.query_params.get('is_developer'):
            if is_developer == 'true':
                return queryset.filter(is_developer=True)
            if is_developer == 'false':
                return queryset.filter(is_developer=False)
            raise ValidationError({'is_developer': "This field must be 'true' or 'false'."})

        return queryset

    def get_serializer_class(self):
        if self.action != 'retrieve':
            return UserSerializer
        return UserDetailSerializer
