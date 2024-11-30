import allure
import pytest

from services.entity.entity_service import EntityService


@allure.feature("Entity 'Superheroes'")
@allure.story("Get entity 'Superheroes'")
@pytest.mark.api
class TestHeroAPI:
    """Test suite for Entity Superheroes API CRUD operations."""

    @allure.title("Test male with work")
    @allure.description("Checking the search for the highest male superhero with work")
    def test_male_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest male superhero with work."""
        with allure.step(f"Retrieving the highest male superhero with work"):
            hero_highest = entity_service.get_hero_highest("Male", True)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Utgard-Loki"

    @allure.title("Test male without work")
    @allure.description("Checking the search for the highest male superhero without work")
    def test_male_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest male superhero without work."""
        with allure.step(f"Retrieving the highest male superhero without work"):
            hero_highest = entity_service.get_hero_highest("Male", False)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Ymir"

    @allure.title("Test female with work")
    @allure.description("Checking the search for the highest female superhero with work")
    def test_female_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest female superhero with work."""
        with allure.step(f"Retrieving the highest female superhero with work"):
            hero_highest = entity_service.get_hero_highest("Female", True)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Giganta"

    @allure.title("Test female without work")
    @allure.description("Checking the search for the highest female superhero without work")
    def test_female_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest female superhero without work."""
        with allure.step(f"Retrieving the highest female superhero without work"):
            hero_highest = entity_service.get_hero_highest("Female", False)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Ardina"

    @allure.title("Test uncertain gender with work")
    @allure.description("Checking the search for the highest uncertain gender superhero with work")
    def test_uncertain_gender_with_work(self, entity_service: EntityService):
        """Test for checking the search for the highest uncertain gender superhero with work."""
        with allure.step(f"Retrieving the highest uncertain gender superhero with work"):
            hero_highest = entity_service.get_hero_highest("-", True)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Living Brain"

    @allure.title("Test uncertain gender without work")
    @allure.description("Checking the search for the highest uncertain gender superhero without work")
    def test_uncertain_gender_without_work(self, entity_service: EntityService):
        """Test for checking the search for the highest uncertain gender superhero without work."""
        with allure.step(f"Retrieving the highest uncertain gender superhero without work"):
            hero_highest = entity_service.get_hero_highest("-", False)
        with allure.step(f"Comparison retrieving entity '{hero_highest['name']}' with the source"):
            assert hero_highest['name'] == "Godzilla"

    @allure.title("Test param error")
    @allure.description("Checking an incorrect parameter")
    @pytest.mark.parametrize("gender, has_job", [
        ("Other", True), ("Other", False), ("Male", "Error"), ("Male", 10), ("Male", 0), ("Male", -10),
        ("", True), ("", False), (True, 10), (False, 10), ("", ""), (0, 0)
    ])
    def test_param_error(self, entity_service: EntityService, gender, has_job):
        """Test for checking the param error."""
        with allure.step(f"Retrieving the highest superhero with param error"):
            hero_highest = entity_service.get_hero_highest(gender, has_job)
        with allure.step(f"Comparison retrieving entity '{hero_highest}' with the source"):
            assert hero_highest is None
