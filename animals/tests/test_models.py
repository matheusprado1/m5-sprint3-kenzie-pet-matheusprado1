from groups.models import Group
from traits.models import Trait
from django.test import TestCase
from animals.models import Animal


class AnimalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.sex_default = "Não informado"

        cls.animal_1_data = {
            "name": "Thor",
            "age": 7,
            "weight": 60,
            "sex": "Macho",
        }

        cls.animal_2_data = {
            "name": "Cacau",
            "age": 9,
            "weight": 15,
            "sex": "Fêmea",
        }

        cls.animal_3_data = {
            "name": "Juju",
            "age": 3,
            "weight": 4,
        }

        cls.animal_1 = Animal.objects.create(**cls.animal_1_data)
        cls.animal_2 = Animal.objects.create(**cls.animal_2_data)
        cls.animal_3 = Animal.objects.create(**cls.animal_3_data)

        group_data_1 = {"name": "Cão",
                        "scientific_name": "Canis lupus familiaris"}
        group_data_2 = {"name": "Gato", "scientific_name": "Felis catus"}

        cls.group_1 = Group(**group_data_1)
        cls.group_2 = Group(**group_data_2)

        trait_data_1 = {"name": "grande porte", "name": "pelo curto"}
        trait_data_2 = {"name": "pequeno porte", "name": "pelo curto"}
        trait_data_3 = {"name": "pequeno porte",
                        "name": "pelo malhado(branco e preto)"}

        cls.trait_1 = Trait(**trait_data_1)
        cls.trait_2 = Trait(**trait_data_2)
        cls.trait_3 = Trait(**trait_data_3)

    # def test_one_to_many_relatinship_with_group(self):
    #     print("Executando test_one_to_one_relatinship_with_group")
    #     self.groups_1.animal = self.animal_1
    #     self.group_1.save()
    #     msg = "Verifique o relacionamento 1:N de animal com group"

    #     self.assertIs(self.animal_1.group, self.group_2, msg)


    def test_animal_fields(self):
        print("executando test_animal_fields")

        self.assertEqual(self.animal_1.name, self.animal_1_data["name"])
        self.assertEqual(self.animal_1.age, self.animal_1_data["age"])
        self.assertEqual(self.animal_1.weigth, self.animal_1_data["weight"])
        self.assertEqual(
            self.animal_1.sex, self.animal_1_data["sex"]
        )
