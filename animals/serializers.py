from email.policy import default
from rest_framework import serializers
from . models import Animal, Sex
from groups.serializers import GroupSerializer
from groups.models import Group
from traits.serializers import TraitSerializer
from traits.models import Trait
import math


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Sex.choices, default=Sex.DEFAULT
    )
    age_in_dog_years = serializers.SerializerMethodField()

    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def get_age_in_dog_years(self, obj : Animal) -> int:

        dog_age = obj.age
        human_age = 16 * math.log(dog_age) + 31
        return human_age

    def create(self, validated_data: dict):

        group = validated_data.pop("group")
        traits = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group)
        animal = Animal.objects.create(**validated_data, group=group)

        for trait in traits:
            trt, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(trt)

        return animal

    def update(self, instace: Animal, validated_data: dict) -> Animal:
        no_editable_keys = ("sex", "group", "traits")

        for key, value in validated_data.items():
            if key in no_editable_keys:
                raise KeyError
            else:
                setattr(instace, key, value)

        instace.save()

        return instace
