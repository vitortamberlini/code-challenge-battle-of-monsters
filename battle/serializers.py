from rest_framework import serializers

from battle.models import Battle

from monster.models import Monster
from monster.serializers import MonsterSerializer


class BattleListSerializer(serializers.ModelSerializer):
    monsterA = MonsterSerializer()
    monsterB = MonsterSerializer()
    winner = MonsterSerializer()

    class Meta:
        model = Battle
        fields = "__all__"


class BattleCreateSerializer(serializers.ModelSerializer):
    monsterA = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(),
        write_only=True,
        error_messages={
            "does_not_exist": "Monster A does not exist.",
            "blank": "This field is required.",
            "null": "This field is required.",
        },
    )
    monsterB = serializers.PrimaryKeyRelatedField(
        queryset=Monster.objects.all(),
        write_only=True,
        error_messages={
            "does_not_exist": "Monster B does not exist.",
            "blank": "This field is required.",
            "null": "This field is required.",
        },
    )
    winner = MonsterSerializer(read_only=True)

    class Meta:
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return {}
