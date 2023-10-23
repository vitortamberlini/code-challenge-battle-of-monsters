from rest_framework import serializers

from battle.models import Battle
from battle.utils import fight
from monster.models import Monster

from monster.nested_serializers import MonsterListRetrieveUpdateSerializer


class BattleListSerializer(serializers.ModelSerializer):
    monsterA = MonsterListRetrieveUpdateSerializer()
    monsterB = MonsterListRetrieveUpdateSerializer()
    winner = MonsterListRetrieveUpdateSerializer()

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):
    monsterA = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(), write_only=True
    )
    monsterB = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(), write_only=True
    )
    winner = MonsterListRetrieveUpdateSerializer(read_only=True)

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        monster_a = validated_data["monsterA"]
        monster_b = validated_data["monsterB"]
        winner = fight(monster_a, monster_b)
        instance = Battle.objects.create(
            **{"monsterA": monster_a, "monsterB": monster_a, "winner": winner}
        )

        return instance
