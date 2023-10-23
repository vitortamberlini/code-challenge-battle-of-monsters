from unittest.mock import Mock

from battle.utils import (
    Creature,
    define_attack_order,
    both_are_alive,
    turn_generator,
    fight,
)
from monster.models import Monster

from battle.tests.test_utils_setup import UtilsSetUp


def add_monsters(monster_a, monster_b):
    monster_list = [Monster(**row) for row in [monster_a, monster_b]]

    Monster.objects.bulk_create(monster_list)


class UtilsTests(UtilsSetUp):
    def test_monster_a_with_higher_speed_fight(self):
        creature_a = Mock(spec=Creature)
        creature_a.speed = 10
        creature_a.attack = 5
        creature_b = Mock(spec=Creature)
        creature_b.speed = 5
        creature_b.attack = 5

        result = define_attack_order(creature_a, creature_b)
        expected = creature_a, creature_b

        self.assertEqual(result, expected)

    def test_monster_b_with_higher_speed_fight(self):
        creature_a = Mock(spec=Creature)
        creature_a.speed = 10
        creature_a.attack = 5
        creature_b = Mock(spec=Creature)
        creature_b.speed = 50
        creature_b.attack = 5

        result = define_attack_order(creature_a, creature_b)
        expected = creature_b, creature_a

        self.assertEqual(result, expected)

    def test_monster_with_equal_speed_and_monster_a_higher_attack_fight(self):
        creature_a = Mock(spec=Creature)
        creature_a.speed = 10
        creature_a.attack = 50
        creature_b = Mock(spec=Creature)
        creature_b.speed = 10
        creature_b.attack = 5

        result = define_attack_order(creature_a, creature_b)
        expected = creature_a, creature_b

        self.assertEqual(result, expected)

    def test_monster_with_equal_speed_and_monster_b_higher_attack_fight(self):
        creature_a = Mock(spec=Creature)
        creature_a.speed = 10
        creature_a.attack = 5
        creature_b = Mock(spec=Creature)
        creature_b.speed = 10
        creature_b.attack = 50

        result = define_attack_order(creature_a, creature_b)
        expected = creature_b, creature_a

        self.assertEqual(result, expected)

    def test_creature_is_not_alive(self):
        creature = Mock(spec=Creature)
        creature.hit_points = 0
        creature.is_alive.side_effect = lambda: Creature.is_alive(creature)

        result = creature.is_alive()

        self.assertEqual(result, False)

    def test_creature_is_alive(self):
        creature = Mock(spec=Creature)
        creature.hit_points = 10
        creature.is_alive.side_effect = lambda: Creature.is_alive(creature)

        result = creature.is_alive()

        self.assertEqual(result, True)

    def test_attack_creature_minimum_damage(self):
        creature_a = Mock(spec=Creature)
        creature_a.attack = 5
        creature_b = Mock(spec=Creature)
        creature_b.defense = 50
        initial_hp = 10
        creature_b.hit_points = initial_hp
        creature_a.attack_creature.side_effect = lambda: Creature.attack_creature(
            creature_a, creature_b
        )

        creature_a.attack_creature()

        self.assertEqual(creature_b.hit_points, 9)

    def test_attack_creature(self):
        creature_a = Mock(spec=Creature)
        creature_a.attack = 10
        creature_b = Mock(spec=Creature)
        creature_b.defense = 5
        initial_hp = 10
        creature_b.hit_points = initial_hp
        creature_a.attack_creature.side_effect = lambda: Creature.attack_creature(
            creature_a, creature_b
        )

        creature_a.attack_creature()

        self.assertEqual(creature_b.hit_points, 5)

    def test_both_are_alive_true(self):
        creature_a = Mock(spec=Creature)
        creature_a.is_alive.side_effect = lambda: True

        creature_b = Mock(spec=Creature)
        creature_b.is_alive.side_effect = lambda: True

        result = both_are_alive(creature_a, creature_b)

        self.assertEqual(result, True)

    def test_both_are_alive_false(self):
        creature_a = Mock(spec=Creature)
        creature_a.is_alive.side_effect = lambda: False

        creature_b = Mock(spec=Creature)
        creature_b.is_alive.side_effect = lambda: True

        result = both_are_alive(creature_a, creature_b)

        self.assertEqual(result, False)

    def test_turn_generator(self):
        creature_a = Mock(spec=Creature)
        creature_b = Mock(spec=Creature)
        turn = turn_generator(creature_a, creature_b)

        expected_a = creature_a, creature_b
        expected_b = creature_b, creature_a

        self.assertEqual(next(turn), expected_a)
        self.assertEqual(next(turn), expected_b)
        self.assertEqual(next(turn), expected_a)

    def test_fight_winner_is_monster_a(self):
        monster_a = Mock(spec=Monster)
        monster_a.hp = 100
        monster_a.speed = 100
        monster_a.attack = 100
        monster_a.defense = 100
        monster_b = Mock(spec=Monster)
        monster_b.hp = 1
        monster_b.speed = 1
        monster_b.attack = 1
        monster_b.defense = 1

        result = fight(monster_a, monster_b)

        self.assertEqual(result, monster_a)

    def test_fight_winner_is_monster_b(self):
        monster_a = Mock(spec=Monster)
        monster_a.hp = 1
        monster_a.speed = 1
        monster_a.attack = 1
        monster_a.defense = 1
        monster_b = Mock(spec=Monster)
        monster_b.hp = 100
        monster_b.speed = 100
        monster_b.attack = 100
        monster_b.defense = 100

        result = fight(monster_a, monster_b)

        self.assertEqual(result, monster_b)
