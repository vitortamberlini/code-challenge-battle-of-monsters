from django.urls import reverse

from rest_framework import status

from battle.models import Battle
from battle.tests.test_api_setup import BattleAPISetUp


class BattleAPITests(BattleAPISetUp):
    def test_battle_monster_a_wins_create(self):
        monster_a_id = 2
        monster_b_id = 1
        payload = {"monsterA": monster_a_id, "monsterB": monster_b_id}
        response = self.client.post(self.url_list_create, payload, format="json")
        json_reponse = response.json()
        battle_id = json_reponse["id"]
        winner_id = json_reponse["winner"]["id"]

        self.assertEqual(winner_id, monster_a_id)

    def test_battle_monster_b_wins_create(self):
        monster_a_id = 1
        monster_b_id = 2
        payload = {"monsterA": monster_a_id, "monsterB": monster_b_id}
        response = self.client.post(self.url_list_create, payload, format="json")
        json_reponse = response.json()
        battle_id = json_reponse["id"]
        winner_id = json_reponse["winner"]["id"]

        self.assertEqual(winner_id, monster_b_id)

    def test_battle_invalid_monsters_dont_exist_create(self):
        monster_a_id = -20
        monster_b_id = 999
        payload = {"monsterA": monster_a_id, "monsterB": monster_b_id}
        response = self.client.post(self.url_list_create, payload, format="json")
        json_reponse = response.json()
        expected_json = {
            "monsterA": ['Invalid pk "-20" - object does not exist.'],
            "monsterB": ['Invalid pk "999" - object does not exist.'],
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json_reponse, expected_json)

    def test_battle_blank_null_monsters_fail_create(self):
        monster_a_id = None
        monster_b_id = None
        payload = {"monsterA": monster_a_id, "monsterB": monster_b_id}
        response = self.client.post(self.url_list_create, payload, format="json")
        json_reponse = response.json()
        expected_json = {
            "monsterA": ["This field may not be null."],
            "monsterB": ["This field may not be null."],
        }

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json_reponse, expected_json)

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
        response = self.client.post(
            self.url_list_create, self.battle_data, format="json"
        )
        json_response = response.json()
        self.update_retrieve_delete = reverse(
            "battle:battle_update_retrieve_delete", kwargs={"pk": json_response["id"]}
        )
        response = self.client.delete(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Battle.objects.count(), 0)

    def test_battle_fail_destroy(self):
        self.update_retrieve_delete = reverse(
            "battle:battle_update_retrieve_delete", kwargs={"pk": 99}
        )
        response = self.client.delete(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
