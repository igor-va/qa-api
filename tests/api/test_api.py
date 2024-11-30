import allure
import pytest

from services.entity.entity_service import EntityService


@allure.epic("Entity Superheroes")
@pytest.mark.api
class TestHeroAPI:
    """Test suite for Entity Superheroes API CRUD operations."""

    @allure.title("Test male with work")
    @allure.description("Checking the search for the highest male superhero with work")
    def test_male_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest male superhero with work."""
        with allure.step(f"Retrieving the highest male superhero with work"):
            highest_hero = entity_service.get_highest_hero("Male", True)
            assert highest_hero['name'] == "Utgard-Loki"

    @allure.title("Test male without work")
    @allure.description("Checking the search for the highest male superhero without work")
    def test_male_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest male superhero without work."""
        with allure.step(f"Retrieving the highest male superhero without work"):
            highest_hero = entity_service.get_highest_hero("Male", False)
            assert highest_hero['name'] == "Ymir"

    @allure.title("Test female with work")
    @allure.description("Checking the search for the highest female superhero with work")
    def test_female_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest female superhero with work."""
        with allure.step(f"Retrieving the highest female superhero with work"):
            highest_hero = entity_service.get_highest_hero("Female", True)
            assert highest_hero['name'] == "Giganta"

    @allure.title("Test female without work")
    @allure.description("Checking the search for the highest female superhero without work")
    def test_female_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest female superhero without work."""
        with allure.step(f"Retrieving the highest female superhero without work"):
            highest_hero = entity_service.get_highest_hero("Female", False)
            assert highest_hero['name'] == "Ardina"

    @allure.title("Test uncertain gender with work")
    @allure.description("Checking the search for the highest uncertain gender superhero with work")
    def test_uncertain_gender_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest uncertain gender superhero with work."""
        with allure.step(f"Retrieving the highest uncertain gender superhero with work"):
            highest_hero = entity_service.get_highest_hero("-", True)
            assert highest_hero['name'] == "Living Brain"

    @allure.title("Test uncertain gender without work")
    @allure.description("Checking the search for the highest uncertain gender superhero without work")
    def test_uncertain_gender_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest uncertain gender superhero without work."""
        with allure.step(f"Retrieving the highest uncertain gender superhero without work"):
            highest_hero = entity_service.get_highest_hero("-", False)
            assert highest_hero['name'] == "Godzilla"

    @allure.title("Test invalid gender with work")
    @allure.description("Checking the search for the highest invalid gender superhero with work")
    def test_invalid_gender_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest invalid gender superhero with work."""
        with allure.step(f"Retrieving the highest invalid gender superhero with work"):
            highest_hero = entity_service.get_highest_hero("Other", True)
            assert highest_hero is None

    @allure.title("Test invalid gender without work")
    @allure.description("Checking the search for the highest invalid gender superhero without work")
    def test_invalid_gender_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest invalid gender superhero without work."""
        with allure.step(f"Retrieving the highest invalid gender without work"):
            highest_hero = entity_service.get_highest_hero("Other", False)
            assert highest_hero is None

    @allure.title("Test boolean error")
    @allure.description("Checking for the boolean error")
    def test_boolean_error(self, entity_service: EntityService):
        """Test for checking the boolean error."""
        with allure.step(f"Retrieving the highest superhero with boolean error"):
            highest_hero = entity_service.get_highest_hero("Male", "Error")
            assert highest_hero is None
