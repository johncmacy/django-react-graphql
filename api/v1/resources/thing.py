from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import Thing

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'

class ThingViewSet(ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
