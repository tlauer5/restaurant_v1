from django.test import TestCase
from django.utils import dateparse
from .models import *

ALL_FIXTURES = [
    "waiters.json",
    "reservations.json",
    "tables.json",
    "chefs.json",
    "orders.json"
]

class WaitersTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_waiter_print(self):
        first_waiter = Waiter.objects.get(pk=1) #(name="Hannah")
        print("\nTestcase test_waiter_print:")
        print(first_waiter)
        print("finished\n")

    def test_waiter_assertEqual(self):
        first_waiter = Waiter.objects.get(pk=2)
        self.assertEqual(first_waiter.lastname, "Limbach")

    def test_create_waiter(self):
        newWaiter = Waiter.objects.create(surname="Hannes", lastname="Hamm")
        print("\nTestcase test_create_waiter:")
        print(newWaiter)
        print("finished\n")




#https://docs.djangoproject.com/en/4.0/topics/testing/overview/