from rest_framework import serializers

from monster.base_serializer import MonsterBaseSerializer
from monster.models import Monster


class MonsterSerializer(MonsterBaseSerializer):
    class Meta:
        model = Monster
        fields = "__all__"


class MonsterFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Monster
        fields = ["file"]
