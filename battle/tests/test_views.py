from django.urls import reverse

from rest_framework import status

from battle.models import Battle
from battle.tests.test_api_setup import BattleAPISetUp


class BattleAPITests(BattleAPISetUp):
    def test_battle_monster_a_wins_create(self):
        # TODO
        return

    def test_battle_monster_b_wins_create(self):
        # TODO
        return

    def test_battle_invalid_monsters_dont_exist_create(self):
        # TODO
        return

    def test_battle_blank_null_monsters_fail_create(self):
        # TODO
        return

    def test_battle_invalid_body_create(self):
        response = self.client.post(
            self.url_list_create, self.monster_a_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Battle.objects.count(), 0)

    def test_battle_successful_list(self):
        response = self.client.get(self.url_list_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_battle_successful_detail(self):
        response = self.client.post(
            self.url_list_create, self.battle_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Battle.objects.count(), 1)

        self.update_retrieve_delete = reverse(
            "battle:battle_update_retrieve_delete", kwargs={"pk": 1}
        )
        response = self.client.get(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["monsterA"]["name"], self.monster_a_data["name"])

    def test_battle_fail_detail(self):
        self.update_retrieve_delete = reverse(
            "battle:battle_update_retrieve_delete", kwargs={"pk": 1}
        )
        response = self.client.get(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_battle_successful_destroy(self):
        # TODO
        return

    def test_battle_fail_destroy(self):
        # TODO
        return
