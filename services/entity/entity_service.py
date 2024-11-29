from requests import Response

from services.entity.api_client import APIClient


class EntityService:
    """High-level service for entity operations with deserialization."""

    def __init__(self, api_client: APIClient) -> None:
        """Initializes the service with the provided API client."""
        self.api_client = api_client

    def get_highest_hero(self, gender, has_job):
        """
        Функция, которая принимает на вход пол и наличие работы (булевое значение)
        и возвращает по этим критериям самого высокого героя.
        """
        response = self.api_client.get_all_entities()
        heroes = response.json()

        highest_hero = None
        max_height = 0

        for hero in heroes:
            # try:
            # print(hero["name"])
            if hero['appearance']['gender'] == gender:
                if has_job and hero['work']['occupation'] != "-":
                    height_cm = hero['appearance']['height'][1]
                    if height_cm != "-" and height_cm != "0 kg":
                        try:
                            height = float(height_cm.replace("cm", ""))
                        except:
                            height = float(height_cm.replace("meters", "")) * 100
                        if height > max_height:
                            max_height = height
                            highest_hero = hero
                if not has_job and hero['work']['occupation'] == "-":
                    height_cm = hero['appearance']['height'][1]
                    if height_cm != "-":
                        try:
                            height = float(height_cm.replace("cm", ""))
                        except:
                            height = float(height_cm.replace("meters", "")) * 100
                        if height > max_height:
                            max_height = height
                            highest_hero = hero
            # except:
            #     continue

        # print(highest_hero["name"])
        # print(max_height)
        return highest_hero
