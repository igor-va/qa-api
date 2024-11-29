import allure
from requests import Response

from .api_endpoints import APIEndpoints
from .http_client import HTTPClient


class APIClient:
    """Low-level API client for interacting with the service."""

    def __init__(self, base_url: str) -> None:
        """Initializes the APIClient with a base URL."""
        self.base_url = base_url
        self.http_client = HTTPClient(base_url)

    @allure.step("Get all entities")
    def get_all_entities(self) -> Response:
        """Gets all entities with the provided filters."""
        return self.http_client.get(APIEndpoints.GET_ALL_ENDPOINT)
