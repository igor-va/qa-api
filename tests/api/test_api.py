import allure
import pytest

from services.entity.entity_service import EntityService


@allure.epic("Entity Management")
@allure.feature("CRUD Operations")
class TestHeroAPI:
    """Test suite for Entity API CRUD operations."""

    # @allure.title("Test get entity")
    # @allure.description("Verify that a specific entity can be retrieved")
    # @pytest.mark.api
    # def test_get_entity(self, entity_service: EntityService, new_entity: EntityResponse) -> None:
    #     """Test that verifies a specific entity can be retrieved."""
    #     with allure.step(f"Retrieving the created entity with ID {new_entity.id}"):
    #         response, retrieved_entity = entity_service.get_entity(str(new_entity.id))
    #         assert (
    #             response.status_code == 200
    #         ), f"Error while retrieving entity: {response.status_code}, {response.text}"
    #
    #     validate_entity(retrieved_entity, new_entity)

    @allure.title("Test get entity")
    @allure.description("Verify that a specific entity can be retrieved")
    @pytest.mark.api
    def test_male_with_job(self, entity_service: EntityService) -> None:
        """Test that verifies a specific entity can be retrieved."""
        with allure.step(f"Retrieving the created entity with ID"):
            highest_hero = entity_service.get_highest_hero("Male", True)
            assert highest_hero['name'] == "Utgard-Loki"

    def test_male_without_job():
        highest_hero = get_highest_hero("Male", False)
        assert highest_hero['name'] == "Ymir"

    def test_female_with_job():
        highest_hero = get_highest_hero("Female", True)
        assert highest_hero['name'] == "Giganta"

    def test_female_without_job():
        highest_hero = get_highest_hero("Female", False)
        assert highest_hero['name'] == "Ardina"

    def test_uncertain_gender_with_job():
        highest_hero = get_highest_hero("-", True)
        assert highest_hero['name'] == "Living Brain"

    def test_uncertain_gender_without_job():
        highest_hero = get_highest_hero("-", False)
        assert highest_hero['name'] == "Godzilla"

    def test_invalid_gender_with_job():
        highest_hero = get_highest_hero("Other", True)
        assert highest_hero is None

    def test_invalid_gender_without_job():
        highest_hero = get_highest_hero("Other", False)
        assert highest_hero is None
