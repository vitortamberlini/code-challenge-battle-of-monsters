from typing import Generator

from monster.models import Monster


# Create your battle Algorithm here


class Creature:
    def __init__(self, monster: Monster):
        self.hit_points = monster.hp
        self.speed = monster.speed
        self.attack = monster.attack
        self.defense = monster.defense

    def is_alive(self):
        return self.hit_points > 0

    def attack_creature(self, defender: "Creature") -> None:
        damage = max(1, self.attack - defender.defense)
        defender.hit_points -= damage


def both_are_alive(creature_a: Creature, creature_b: Creature) -> bool:
    return creature_a.is_alive() and creature_b.is_alive()


def define_attack_order(
    creature_a: Creature, creature_b: Creature
) -> tuple[Creature, Creature]:
    if (creature_a.speed, creature_a.attack) > (creature_b.speed, creature_b.attack):
        return creature_a, creature_b
    return creature_b, creature_a


def turn_generator(
    creature_a: Creature, creature_b: Creature
) -> Generator[tuple[Creature, Creature], None, None]:
    first, second = creature_a, creature_b
    while True:
        yield first, second
        yield second, first


def fight(monster_a: Monster, monster_b: Monster) -> Monster:
    creature_a = Creature(monster_a)
    creature_b = Creature(monster_b)
    turn = turn_generator(*define_attack_order(creature_a, creature_b))

    while both_are_alive(creature_a, creature_b):
        attacker, defender = next(turn)

        attacker.attack_creature(defender)

    if creature_a.is_alive():
        winner = monster_a
    else:
        winner = monster_b

    return winner
