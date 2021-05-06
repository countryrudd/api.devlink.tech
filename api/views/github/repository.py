from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from services import github
from services.github.exceptions import GitHubApiError


class RepositoryView(APIView):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head']

    def get(self, request, *args, **kwargs):
        try:
            return Response(github.get_repositories(self.request.query_params.get('github_username')))
        except GitHubApiError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
