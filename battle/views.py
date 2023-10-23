from rest_framework import mixins, viewsets

from battle.models import Battle
from battle.serializers import BattleListSerializer, BattleCreateSerializer


# Create your views here.
class BattleListCreateView(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    A simple ViewSet for listing battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListSerializer
    serializer_create_class = BattleCreateSerializer
    pagination_class = None
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "create":
            return self.serializer_create_class
        return self.serializer_class


class BattleRetrieveDeleteView(
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    """
    A simple ViewSet for update, retrieve and delete battles.
    """

    queryset = Battle.objects.all()
    serializer_class = BattleListSerializer
    authentication_classes = []
    permission_classes = []
