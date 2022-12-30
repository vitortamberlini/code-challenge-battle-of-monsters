from django.urls import reverse

from rest_framework import status

from monster.models import Monster
from monster.tests.test_api_setup import MonsterAPISetUp


class MonsterAPITests(MonsterAPISetUp):
    def test_monster_successful_import(self):
        # TODO
        return

    def test_monster_empty_import(self):
        # TODO
        return

    def test_monster_wrong_import(self):
        # TODO
        return

    def test_monster_successful_create(self):
        response = self.client.post(
            self.url_list_create, self.monster_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Monster.objects.count(), 6)

    def test_monster_fail_create(self):
        data = self.monster_data.copy()
        data["hp"] = 200

        response = self.client.post(self.url_list_create, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"hp": ["Ensure this value is less than or equal to 100."]}
        )
        self.assertEqual(Monster.objects.count(), 5)

    def test_monster_successful_list(self):
        response = self.client.get(self.url_list_create, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_monster_successful_detail(self):
        monster = Monster.objects.create(**self.monster_data)
        monster.save()

        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 6}
        )
        response = self.client.get(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], monster.name)

    def test_monster_fail_detail(self):
        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 6}
        )
        response = self.client.get(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_monster_successful_update(self):
        monster = Monster.objects.create(**self.monster_data)
        monster.save()

        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 6}
        )

        data_update = {"name": "New name"}

        response = self.client.put(
            self.update_retrieve_delete, data_update, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data["name"], monster.name)
        self.assertEqual(response.data["name"], data_update.get("name"))

    def test_monster_fail_update(self):
        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 5}
        )

        data_update = {"hp": 201}

        response = self.client.put(
            self.update_retrieve_delete, data_update, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"hp": ["Ensure this value is less than or equal to 100."]}
        )

    def test_monster_successful_destroy(self):
        monster = Monster.objects.create(**self.monster_data)
        monster.save()

        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 6}
        )

        response = self.client.delete(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_monster_fail_destroy(self):
        self.update_retrieve_delete = reverse(
            "monster:monster_update_retrieve_delete", kwargs={"pk": 6}
        )

        response = self.client.delete(self.update_retrieve_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
