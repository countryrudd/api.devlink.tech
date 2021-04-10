import pytest
from rest_framework.test import APIClient


def refresh_all_from_db(*args):
    for model in args:
        if getattr(model, 'refresh_from_db'):
            model.refresh_from_db()
    return args


@pytest.fixture(autouse=True)
def disable_network_access(monkeypatch):
    """Prevent any un-mocked network requests from executing in tests"""

    def fail(*args, **kwargs):
        pytest.fail('Called network method in test')

    monkeypatch.setattr('socket.socket', fail)


@pytest.fixture
def api_client():
    client = APIClient()
    client.default_format = 'json'
    return client
