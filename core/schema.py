import graphene
from graphene_django.types import DjangoObjectType
from .models import Thing

class ThingType(DjangoObjectType):
    class Meta:
        model = Thing

class Query(graphene.ObjectType):
    all_things = graphene.List(ThingType)

    def resolve_all_things(self, info, **kwargs):
        return Thing.objects.all()
