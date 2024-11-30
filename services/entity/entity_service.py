from services.entity.api_client import APIClient


class EntityService:
    """High-level service for entity operations."""

    def __init__(self, api_client: APIClient) -> None:
        """Initializes the service with the provided API client."""
        self.api_client = api_client

    def get_hero_highest(self, gender, has_job):
        """
        A function that takes the entrance of the gender and the availability of work (boolean value)
        and he returns according to these criteria of the highest hero.

        :param gender: "Male", "Female", "-"
        :param has_job: True, False
        :return: The highest hero that matches the criteria, or None if no hero matches
        """
        try:
            response = self.api_client.get_all_entities()
            heroes = response.json()

            hero_highest = None
            hero_max_height = 0

            for hero in heroes:
                if hero['appearance']['gender'] == gender:
                    if (has_job is True and hero['work']['occupation'] != "-") or \
                            (has_job is False and hero['work']['occupation'] == "-"):
                        hero_api_height = hero['appearance']['height'][1]
                        if "cm" in hero_api_height:
                            hero_cur_height = float(hero_api_height.replace(" cm", ""))
                        elif "meters" in hero_api_height:
                            hero_cur_height = float(hero_api_height.replace(" meters", "")) * 100
                        else:
                            continue
                        if hero_cur_height > hero_max_height:
                            hero_max_height = hero_cur_height
                            hero_highest = hero
            return hero_highest
        except Exception as e:
            print(f"An error occurred: {e}")
            return None  # Return None explicitly in case of error
