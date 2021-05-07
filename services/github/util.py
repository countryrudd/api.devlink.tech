import requests
from django.conf import settings
from requests import Response

from .exceptions import *

api_url_base = 'https://api.github.com'

request_headers = {
    'Authorization': 'token ' + settings.GITHUB_API_KEY
}


def github_request(method: str, path: str, on_behalf_of: str = '', **kwargs) -> Response:
    """
    Wrapper for `requests.request()` with `GitHubApiError` handling.
    """
    if on_behalf_of:
        request_headers['on-behalf-of'] = on_behalf_of
    response = requests.request(method, api_url_base + path,
                                headers=request_headers,
                                timeout=settings.REQUESTS_TIMEOUT,
                                **kwargs)
    try:
        response.raise_for_status()
    except Exception:
        raise GitHubApiError(response)

    return response
