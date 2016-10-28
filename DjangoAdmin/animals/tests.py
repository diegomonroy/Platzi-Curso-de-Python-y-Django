from django.test import TestCase
from .models import Animal

# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="Pedro", last_name="Hernandez")

    def test_animals_have_last_name(self):
        pedro = Animal.objects.get(name="Pedro")

        self.assertEqual(pedro.last_name, "Hernandez")