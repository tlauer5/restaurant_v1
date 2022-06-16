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
        inProgressOrders = Order.objects.filter(waiter=waiter_pk, status=Order.OrderStatus.IN_PROGRESS)
        cookedOrders = Order.objects.filter(status=Order.OrderStatus.COOKED)
        deliveredOrders = Order.objects.filter(waiter=waiter_pk, status=Order.OrderStatus.DELIVERED)
        billedOrders = Order.objects.filter(waiter=waiter_pk, status=Order.OrderStatus.BILLED)

        for order in cookedOrders:
            print(order.info_for_waiter())

    def test_delete_order(self):
        return


class ChefsTests(TestCase):
    fixtures = ALL_FIXTURES

    def test_show_unassigned_orders(self):

        unassigned_orders = Order.objects.filter(status=Order.OrderStatus.UNASSIGNED)

        for order in unassigned_orders:
            print(order.info_for_chef())

    def test_assign_order_to_chef(self):
        new_order_pk = 1

        unassigned_orders = Order.objects.filter(status=Order.OrderStatus.UNASSIGNED)

        if not unassigned_orders.exists():
            return

        order_to_assign_pk = unassigned_orders[0].pk

        print('PK: ' + str(order_to_assign_pk) + '\n')

        # Current PK and Status
        print(Order.objects.filter(pk=order_to_assign_pk)[0].info_for_chef())

        # Update PK and Status
        Order.objects.filter(pk=order_to_assign_pk).update(chef=new_order_pk, status=Order.OrderStatus.IN_PROGRESS)

        # Updated PK and Status
        print(Order.objects.filter(pk=order_to_assign_pk)[0].info_for_chef())



    def test_getNewOrder(self):
        pass

    def test_update_order(self):
        pass

        #for order in qSet:
         #   print(order)
         #  print("\n")








#https://docs.djangoproject.com/en/4.0/topics/testing/overview/

#pk über namen herausfinden
#new_chef_pk = Chef.objects.filter(surname="Kurt", lastname="Lamm")[0].pk
#am besten noch prüfen ob nur einer in Liste ist oder ob überhaupt jemand mit dem Namen gefunden wurde