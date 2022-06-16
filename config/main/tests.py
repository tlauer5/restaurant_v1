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

    def test_showAllOrders(self):
        waiter_pk = 1
        unassignedOrders = Order.objects.filter(waiter=waiter_pk, status=Order.OrderStatus.UNASSIGNED)
        inProgressOrders = Order.objects.filter(chef=waiter_pk, status=Order.OrderStatus.IN_PROGRESS)
        cookedOrders = Order.objects.filter(chef=waiter_pk, status=Order.OrderStatus.COOKED)
        deliveredOrders = Order.objects.filter(chef=waiter_pk, status=Order.OrderStatus.DELIVERED)
        billedOrders = Order.objects.filter(chef=waiter_pk, status=Order.OrderStatus.BILLED)



    def test_deleteOrder(self):
        pass


class ChefsTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_myOpenOrders(self):
        chef_pk = 2
        for order in Order.objects.filter(chef=chef_pk, status=Order.OrderStatus.IN_PROGRESS):
            print(order)

    def test_getNewOrder(self):
        pass

    def test_updateOrder(self):
        pass

        #for order in qSet:
         #   print(order)
         #  print("\n")








#https://docs.djangoproject.com/en/4.0/topics/testing/overview/