from django.db.models import ForeignKey
from django.test import TestCase

from monster.models import Monster

from battle.models import Battle

from utils.utils import monster_b_data


# Create your tests here.


def create_dummy_monster(monster_a, monster_b, winner):
    battle_data = {
        "monsterA": monster_a,
        "monsterB": monster_b,
        "winner": winner,
    }

    Battle.objects.create(**battle_data)
    return Battle.objects.get(id=2)


class BattleModelTests(TestCase):
    data = monster_b_data

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        data = cls.data.copy()
        data["id"] = 6
        monster = Monster.objects.create(**data)

        monsters = Monster.objects.all()

        data = {
            "monsterA": monsters.first(),
            "monsterB": monster,
            "winner": monsters.first(),
        }

        Battle.objects.create(**data)

    def test_verbose_name(self):
        self.assertEqual(str(Battle._meta.verbose_name), "Battle")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Battle._meta.verbose_name_plural), "Battles")

    def test_foreign_keys(self):
        fks = [f for f in Battle._meta.fields if isinstance(f, ForeignKey)]
        self.assertEqual(len(fks), 3)
        self.assertEqual(fks[0].name, "monsterA")
        self.assertEqual(fks[1].name, "monsterB")
        self.assertEqual(fks[2].name, "winner")

    def test_monsterA_label(self):
        battle = Battle.objects.get(id=1)
        field_label = battle._meta.get_field("monsterA").verbose_name
        self.assertEqual(field_label, "Monster A")

    def test_monsterA_value(self):
        monsters = Monster.objects.all()
        first_monster = monsters.first()
        last_monster = monsters.last()
        battle = create_dummy_monster(first_monster, last_monster, first_monster)

        self.assertEqual(battle.monsterA.name, first_monster.name)

    def test_monsterB_label(self):
        battle = Battle.objects.get(id=1)
        field_label = battle._meta.get_field("monsterB").verbose_name
        self.assertEqual(field_label, "Monster B")

    def test_monsterB_value(self):
        monsters = Monster.objects.all()
        first_monster = monsters.first()
        last_monster = monsters.last()
        battle = create_dummy_monster(first_monster, last_monster, first_monster)

        self.assertEqual(battle.monsterB.name, last_monster.name)

    def test_winner_label(self):
        battle = Battle.objects.get(id=1)
        field_label = battle._meta.get_field("winner").verbose_name
        self.assertEqual(field_label, "Winner")

    def test_winner_value(self):
        monsters = Monster.objects.all()
        first_monster = monsters.first()
        last_monster = monsters.last()
        battle = create_dummy_monster(first_monster, last_monster, first_monster)

        self.assertEqual(battle.winner.name, first_monster.name)
