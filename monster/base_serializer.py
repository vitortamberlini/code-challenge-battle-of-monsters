from rest_framework import serializers

from monster.models import Monster

from utils.utils import CustomCharField


class MonsterBaseSerializer(serializers.ModelSerializer):
    name = CustomCharField(
        max_length=100,
        allow_blank=False,
    )

    speed = serializers.IntegerField(min_value=0, max_value=100)

    attack = serializers.IntegerField(min_value=0, max_value=100)

    defense = serializers.IntegerField(min_value=0, max_value=100)

    hp = serializers.IntegerField(min_value=0, max_value=100)

    imageUrl = serializers.URLField()

    class Meta:
        model = Monster
        fields = "__all__"
