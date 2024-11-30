import pytest

from config.config_api.config import Config
from services.entity.api_client import APIClient
from services.entity.entity_service import EntityService


@pytest.fixture
def api_client() -> APIClient:
    """Fixture to create and return an APIClient instance."""
    return APIClient(Config.BASE_URL)


@pytest.fixture
def entity_service(api_client: APIClient) -> EntityService:
    """Fixture for creating an EntityService instance."""
    return EntityService(api_client)

