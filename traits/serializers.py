from rest_framework import serializers
from . models import Trait

class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data: dict):
        return Trait.objects.create(**validated_data)