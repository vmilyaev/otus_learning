import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL for testing")
    parser.addoption("--status_code", action="store", default="200", help="Expected status code")


def test_url_status(request):
    url = request.config.getoption("--url", default="https://ya.ru")
    status_code = int(request.config.getoption("--status_code", default="200"))

    response = requests.get(url)

    assert response.status_code == status_code
