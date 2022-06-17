from datetime import datetime

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

    def test_create_order(self):
        # Number of Orders before
        all_orders = Order.objects.filter()

        if not all_orders.exists():
            return

        number_of_orders_before = all_orders.count()

        Order.objects.create(waiter_id=3,
                             table_id=13,
                             chef_id=None,
                             timestamp=datetime.now(),
                             status=Order.OrderStatus.UNASSIGNED,
                             dish_ID=63,
                             extra_wishes='extra pepper')

        number_of_orders_after = all_orders.count()

        if number_of_orders_after > number_of_orders_before:
            print('\n\nSuccessfully created new order!\n' + \
                  'Orders before: ' + str(number_of_orders_before) + \
                  ' - Orders after: ' + str(number_of_orders_after))

    def test_show_cooked_orders(self):
        cookedOrders = Order.objects.filter(status=Order.OrderStatus.COOKED)

        for order in cookedOrders:
            print(order.info_for_waiter())

    def test_delete_order(self):
        # Number of Orders before
        all_orders = Order.objects.filter()

        if not all_orders.exists():
            return

        number_of_orders_before = all_orders.count()

        orderToDeletePk = 4

        Order.objects.filter(pk=orderToDeletePk).delete()

        number_of_orders_after = all_orders.count()

        if number_of_orders_after < number_of_orders_before:
            print('\n\nSuccessfully deleted an order!\n' + \
                  'Orders before: ' + str(number_of_orders_before) + \
                  ' - Orders after: ' + str(number_of_orders_after))

    def test_create_reservation(self):
        allReservations = Reservation.objects.filter()

        if not allReservations.exists():
            return

        numberOfReservationsBefore = allReservations.count()

        firstTablePk, secondTablePk= 15, 16
        newReservation = Reservation.objects.create(customer_name='Mayer',
                                                    timestamp="2022-05-27T18:00:00.00Z",
                                                    places=8)

        newReservation.table.set([firstTablePk, secondTablePk])
        #oder auch mit .add(15) -> man muss erst Instanz erstellen bevor man many to many field beschreiben kann...

        #print(newReservation)

        numberOfReservationsAfter = allReservations.count()

        if numberOfReservationsAfter > numberOfReservationsBefore:
            print('\n\nSuccessfully created new order!\n' + \
                  'Orders before: ' + str(numberOfReservationsBefore) + \
                  ' - Orders after: ' + str(numberOfReservationsAfter))

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

        # Current PK and Status
        print(Order.objects.filter(pk=order_to_assign_pk)[0].info_for_chef())

        # Update PK and Status
        Order.objects.filter(pk=order_to_assign_pk).update(chef=new_order_pk, status=Order.OrderStatus.IN_PROGRESS)

        # Updated PK and Status
        print(Order.objects.filter(pk=order_to_assign_pk)[0].info_for_chef())


class AdminsTest(TestCase):
    fixtures = ALL_FIXTURES

    def test_admin_create_new_waiter(self):
        # Number of Waiters before
        allWaiters = Waiter.objects.filter()

        numberOfWaitersBefore = allWaiters.count()

        if not allWaiters.exists():
            return

        Waiter.objects.create(surname="Mario",
                              lastname="Kluge")

        numberOfWaitersAfter = allWaiters.count()

        if numberOfWaitersAfter > numberOfWaitersBefore:
            print('\n\nSuccessfully created new order!\n' + \
                  'Waiters before: ' + str(numberOfWaitersBefore) + \
                  ' - Waiters after: ' + str(numberOfWaitersAfter))





# https://docs.djangoproject.com/en/4.0/topics/testing/overview/

# pk oder anderes über namen herausfinden -> man erhält von filter ein queryset zurück (darüber kann man iterieren (for order in querySetOrder:..))
# new_chef_pk = Chef.objects.filter(surname="Kurt", lastname="Lamm")[0].pk
# am besten noch prüfen ob nur einer in Liste ist oder ob überhaupt jemand mit dem Namen gefunden wurde

# assertEqual zum Vergleich


# mit objects.get erhält man Objekt zurück das darauf passt (Achtung: nur eins -sonst fehler)
# Order.objects.get(pk=2)
# Order.objects.get(dish_ID=2)


# neues Objekt anlegen welches auf foreignKeys zurückgreift -> mit foreignkey_id
# new_order = Order.objects.create(waiter_id=3) ->waiter ist foreignkey....
