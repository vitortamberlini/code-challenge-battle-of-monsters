from django.db import IntegrityError
from django.test import TestCase
from django.core import exceptions

from monster.models import Monster

from utils.utils import monster_b_data


# Create your tests here.


class MonsterModelTests(TestCase):
    data = monster_b_data

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        data = cls.data.copy()
        data["id"] = 6
        Monster.objects.create(**data)

    def test_verbose_name(self):
        self.assertEqual(str(Monster._meta.verbose_name), "Monster")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Monster._meta.verbose_name_plural), "Monsters")

    def test_unique_constraint(self):
        data = self.data.copy()
        data["id"] = 6

        with self.assertRaises(IntegrityError) as context:
            Monster.objects.create(**data)

        self.assertTrue("UNIQUE constraint failed" in str(context.exception))

    def test_object_name(self):
        monster = Monster.objects.get(id=6)
        expected_object_name = monster.name
        self.assertEqual(str(monster), expected_object_name)

    def test_name_label(self):
        monster = Monster.objects.get(id=6)
        field_label = monster._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "Name")

    def test_name_value(self):
        monster = Monster.objects.get(id=6)
        self.assertEqual(monster.name, "Dead Unicorn")

    def test_speed_label(self):
        monster = Monster.objects.get(id=6)
        field_label = monster._meta.get_field("speed").verbose_name
        self.assertEqual(field_label, "Speed")

    def test_speed_value(self):
        monster = Monster.objects.get(id=6)
        self.assertEqual(monster.speed, 80)

    def test_attack_label(self):
        monster = Monster.objects.get(id=6)
        field_label = monster._meta.get_field("attack").verbose_name
        self.assertEqual(field_label, "Attack")

    def test_attack_value(self):
        monster = Monster.objects.get(id=6)
        self.assertEqual(monster.attack, 60)

    def test_defense_label(self):
        monster = Monster.objects.get(id=6)
        field_label = monster._meta.get_field("defense").verbose_name
        self.assertEqual(field_label, "Defense")

    def test_defense_value(self):
        monster = Monster.objects.get(id=6)
        self.assertEqual(monster.defense, 40)

    def test_hp_label(self):
        monster = Monster.objects.get(id=6)
        field_label = monster._meta.get_field("hp").verbose_name
        self.assertEqual(field_label, "Hp")

    def test_hp_value(self):
        monster = Monster.objects.get(id=6)
        self.assertEqual(monster.hp, 10)

    def test_int_values_validators(self):
        data = self.data.copy()
        data["id"] = 7
        data["attack"] = 200

        instance = Monster(**data)

        try:
            instance.full_clean()
        except exceptions.ValidationError as error:
            self.assertTrue(
                "Ensure this value is less than or equal to 100" in str(error)
            )

    def test_url_validator(self):
        data = self.data.copy()
        data["id"] = 7
        data["imageUrl"] = "200"

        instance = Monster(**data)

        try:
            instance.full_clean()
        except exceptions.ValidationError as error:
            self.assertTrue("Enter a valid URL" in str(error))
