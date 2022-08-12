from functools import partial
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response, status


from .serializers import AnimalSerializer
from .models import Animal


class AnimalView(APIView):
    def get(self, request) -> Response:
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class AnimalViewById(APIView):
    def get(self, request, id) -> Response:
        animal = get_object_or_404(Animal, id=id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def patch(self, request, id) -> Response:
        animal = get_object_or_404(Animal, id=id)
        serializer = AnimalSerializer(animal, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except KeyError:
            return Response(
                {
                    "message": f"You can not update {list(request.data)[0]} property."
                },
                status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        return Response(serializer.data)

    def delete(self, request, id) -> Response:
        animal = get_object_or_404(Animal, id=id)
        animal_delet = animal.delete()
        return Response(animal_delet, status.HTTP_204_NO_CONTENT)