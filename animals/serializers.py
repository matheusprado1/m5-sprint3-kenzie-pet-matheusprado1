from rest_framework import serializers
from . models import Animal
from groups.serializers import GroupSerializer
from groups.models import Group
from traits.serializers import TraitSerializer
from traits.models import Trait


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    # group = GroupSerializer()
    # traits = TraitSerializer(many=True)

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)
        # group = validated_data.pop("group")
        # traits = validated_data.pop("traits")

        # group, _ = Group.objects.get_or_create(**group)
        # animal = Animal.objects.create(**validated_data, group=group)

        # for trait in traits:
        #     trt, _ = Trait.objects.get_or_create(**trait)
        #     animal.traits.add(trt)

        # return animal
