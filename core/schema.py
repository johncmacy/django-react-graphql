from django.db.models.query import Prefetch
from rest_framework import serializers
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation
from django import forms
from graphene_django.types import DjangoObjectType
from .models import Color, Shape, Thing, Widget
from graphene_django.forms.mutation import DjangoModelFormMutation

from django.contrib.auth import get_user_model
User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]

class ThingType(DjangoObjectType):
    class Meta:
        model = Thing
        fields = [
            'id',
            'name',
            'user',
            'widgets',
        ]

class WidgetType(DjangoObjectType):
    class Meta:
        model = Widget
        fields = [
            'id',
            'thing',
            'shape',
            'color',
            'number',
        ]

class ShapeType(DjangoObjectType):
    class Meta:
        model = Shape
        fields = [
            'id',
            'name',
        ]

class ColorType(DjangoObjectType):
    class Meta:
        model = Color
        fields = [
            'id',
            'name',
        ]

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_things = graphene.List(ThingType)
    all_widgets = graphene.List(WidgetType)
    all_shapes = graphene.List(ShapeType)
    all_colors = graphene.List(ColorType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_things(self, info, **kwargs):
        return Thing.objects.select_related('user').prefetch_related('widgets').all()

    def resolve_all_widgets(self, info, **kwargs):
        return Widget.objects.select_related('thing__user').select_related('shape').select_related('color').all()

    def resolve_all_colors(self, info, **kwargs):
        return Color.objects\
            .prefetch_related(
                Prefetch(
                    lookup='widgets', 
                    queryset=Widget.objects.select_related('thing__user')
                )
            ).all()

    def resolve_all_shapes(self, info, **kwargs):
        return Shape.objects\
            .prefetch_related(
                Prefetch(
                    lookup='widgets', 
                    queryset=Widget.objects.select_related('thing__user')
                )
            ).all()



class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'user',]

class ThingMutation(DjangoModelFormMutation):
    thing = graphene.Field(ThingType)

    class Meta:
        form_class = ThingForm

class Mutation(graphene.ObjectType):
    mutate_thing = ThingMutation.Field()
