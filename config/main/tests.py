from django.test import TestCase
from django.utils import dateparse
from .models import *

ALL_FIXTURES = [
    "waiters.json"
]

class WaitersTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_waiter_print(self):
        first_waiter = Waiter.objects.get(pk=1)
        print(first_waiter)

    def test_waiter_print2(self):
        first_waiter = Waiter.objects.get(pk=1)
        self.assertTrue(first_waiter.__str__())


    def test_waiter_assertEqual(self):
        first_waiter = Waiter.objects.get(pk=2)
        self.assertEqual(first_waiter.surname, "Limbach")



#https://docs.djangoproject.com/en/4.0/topics/testing/overview/