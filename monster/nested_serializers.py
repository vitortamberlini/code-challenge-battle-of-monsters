from django.db.models import Q
from rest_framework import serializers

from battle.models import Battle
from battle.nested_serializers import BattleListPKSerializer

from monster.base_serializer import MonsterBaseSerializer
from monster.models import Monster


class MonsterListRetrieveUpdateSerializer(MonsterBaseSerializer):
    battles = serializers.SerializerMethodField("get_monster_battles")

    def get_monster_battles(self, obj):
        array = [
            BattleListPKSerializer(item).data
            for item in Battle.objects.filter(Q(monsterA=obj) | Q(monsterB=obj))
        ]

        return array

    class Meta:
        model = Monster
        fields = "__all__"
