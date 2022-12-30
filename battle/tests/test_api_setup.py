from django.urls import reverse

from rest_framework.test import APITestCase

from monster.models import Monster

from utils.utils import monster_a_data, monster_b_data


class BattleAPISetUp(APITestCase):
    monster_a_data = monster_a_data

    monster_b_data = monster_b_data

    def setUp(self):
        monster_list = [
            Monster(**row) for row in [self.monster_a_data, self.monster_b_data]
        ]

        Monster.objects.bulk_create(monster_list)

        self.battle_data = {
            "monsterA": self.monster_a_data["id"],
            "monsterB": self.monster_b_data["id"],
        }

        self.url_list_create = reverse("battle:battle_list_create")

        return super().setUp()
