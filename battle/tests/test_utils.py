from monster.models import Monster

from battle.tests.test_utils_setup import UtilsSetUp


def add_monsters(monster_a, monster_b):
    monster_list = [Monster(**row) for row in [monster_a, monster_b]]

    Monster.objects.bulk_create(monster_list)


class UtilsTests(UtilsSetUp):
    def test_monster_a_with_higher_speed_fight(self):
        # TODO
        return

    def test_monster_b_with_higher_speed_fight(self):
        # TODO
        return

    def test_monster_with_equal_speed_and_monster_a_higher_attack_fight(self):
        # TODO
        return

    def test_monster_with_equal_speed_and_monster_b_higher_attack_fight(self):
        # TODO
        return
