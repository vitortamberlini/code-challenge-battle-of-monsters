from rest_framework import serializers

from battle.models import Battle


class BattleListPKSerializer(serializers.ModelSerializer):
    monsterA = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    monsterB = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    winner = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Battle
        fields = "__all__"
