from groups.models import Group
from traits.models import Trait
from django.test import TestCase
from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.animal_1_data = {
            "name": "Thor",
            "age": 7,
            "weight": 40,
            "sex": "Macho",
            "group": {"name": "cão",
                      "scientific_name": "Canis lupus familiaris"},
            "traits": [{"name": "grande porte", "name": "pelo curto"}]
        }
        serializer = AnimalSerializer(data=cls.animal_1_data)

        serializer.is_valid(raise_exception=True)

        cls.animal_1 = serializer.save()

        cls.group_1_data = {
            "name" : "gato",
            "scientific_name" : "Felis catus"
        }
        cls.group_1 = Group.objects.create(**cls.group_1_data)

        cls.trait_1_data = {
            "name" : "pequeno porte"
        }
        cls.trait_1 = Trait.objects.create(**cls.trait_1_data)


    def test_animal_name_max_length(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        max_length = animal._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_animal_age_label(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        field_label = animal._meta.get_field("age").verbose_name
        self.assertEquals(field_label, "age")

    def test_weight_label(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        field_label = animal._meta.get_field("weight").verbose_name
        self.assertEquals(field_label, "weight")

    def test_sex_label(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        field_label = animal._meta.get_field("sex").verbose_name
        self.assertEquals(field_label, "sex")

    def test_create_animal(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        self.assertEquals(animal.name, self.animal_1.name)
        self.assertEquals(animal.age, self.animal_1.age)
        self.assertEquals(animal.weight, self.animal_1.weight)
        self.assertEquals(animal.sex, self.animal_1.sex)

    def test_create_animal_sex_default(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        self.assertEquals(animal.name, self.animal_1.name)
        self.assertEquals(animal.age, self.animal_1.age)
        self.assertEquals(animal.weight, self.animal_1.weight)

    def test_animal_repr(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        self.assertEquals(repr(animal), f"{animal.name} - {animal.age} - {animal.weight} - {animal.sex}")

    def test_group_name_max_lenght(self):
        group = Group.objects.get(id=self.animal_1.id)
        max_length = group._meta.get_field("name").max_length
        self.assertEquals(max_length, 20)

    def test_group_scientific_name_max_lenght(self):
        group = Group.objects.get(id=self.animal_1.id)
        max_length = group._meta.get_field("scientific_name").max_length
        self.assertEquals(max_length, 50)

    def test_group_repr(self):
        group = Group.objects.get(id=self.animal_1.id)
        self.assertEquals(repr(group), f"{group.name} - {group.scientific_name}")

    def test_trait_name_max_lenght(self):
        trait = Trait.objects.get(id=self.animal_1.id)
        max_length = trait._meta.get_field("name").max_length
        self.assertEquals(max_length, 20)

    def test_trait_repr(self):
        trait = Trait.objects.get(id=self.animal_1.id)
        self.assertEquals(repr(trait), f"{trait.name}")

    def test_animal_group_relationship(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        group = Group.objects.get(id=self.animal_1.group.id)
        self.assertEquals(animal.group, group)

    def test_animal_traits_relationship(self):
        animal = Animal.objects.get(id=self.animal_1.id)
        trait = Trait.objects.get(id=self.animal_1.traits.first().id)
        self.assertEquals(animal.traits.first(), trait)
