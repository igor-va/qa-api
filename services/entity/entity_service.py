from services.entity.api_client import APIClient


class EntityService:
    """High-level service for entity operations."""

    def __init__(self, api_client: APIClient) -> None:
        """Initializes the service with the provided API client."""
        self.api_client = api_client

    def get_highest_hero(self, gender, has_job):
        """
        A function that takes the entrance of the gender and the availability of work (boolean value)
        and he returns according to these criteria of the highest hero.

        :param gender: "Male", "Female", "-"
        :param has_job: True, False
        """

        response = self.api_client.get_all_entities()
        heroes = response.json()

        highest_hero = None
        max_height = 0

        for hero in heroes:
            # try:
            # print(hero["name"])
            if hero['appearance']['gender'] == gender:
                if has_job == True and hero['work']['occupation'] != "-":
                    height_cm = hero['appearance']['height'][1]
                    if height_cm != "-" and height_cm != "0 kg":
                        try:
                            height = float(height_cm.replace("cm", ""))
                        except:
                            height = float(height_cm.replace("meters", "")) * 100
                        if height > max_height:
                            max_height = height
                            highest_hero = hero
                if has_job == False and hero['work']['occupation'] == "-":
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
