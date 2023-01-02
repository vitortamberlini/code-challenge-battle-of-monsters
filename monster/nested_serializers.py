from django.db.models import Q
from rest_framework import serializers

from battle.models import Battle
from battle.nested_serializers import BattleListPKSerializer
from monster.models import Monster

from utils.utils import CustomCharField


class MonsterListRetrieveUpdateSerializer(serializers.ModelSerializer):
    name = CustomCharField(
        max_length=100,
        allow_blank=False,
    )

    speed = serializers.IntegerField(min_value=0, max_value=100)

    attack = serializers.IntegerField(min_value=0, max_value=100)

    defense = serializers.IntegerField(min_value=0, max_value=100)

    hp = serializers.IntegerField(min_value=0, max_value=100)

    imageUrl = serializers.URLField()

    battles = serializers.SerializerMethodField('get_monster_battles')

    def get_monster_battles(self, obj):
        array = [BattleListPKSerializer(item).data for item in Battle.objects.filter(
            Q(monsterA=obj) | Q(monsterB=obj)
        )]

        return array

    class Meta:
        model = Monster
        fields = "__all__"
