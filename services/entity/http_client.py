from typing import Any

import requests

from config.config_api.config import Config


class HTTPClient:
    """HTTP client for making requests to a specified base URL."""

    def __init__(self, base_url: str) -> None:
        """Initializes the HTTPClient with a base URL."""
        self.base_url = base_url

    def get(self, endpoint: str) -> requests.Response:
        """Sends a GET request to the specified endpoint with the provided data."""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, timeout=Config.TIMEOUT)
        return response
