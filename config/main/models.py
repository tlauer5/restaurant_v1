from django.db import models


# Model Waiter
class Waiter(models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return str(self.surname) + ' ' + str(self.lastname)


# Model Chef
class Chef(models.Model):
    surname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.surname) + ' ' + str(self.lastname)


# Model Table
class Table(models.Model):
    tableNumber = models.IntegerField(default=None, null=True)
    places = models.IntegerField(default=None, null=True)

    def __str__(self):
        return '\nTable: ' + str(self.tableNumber) + '\n\n'


# Model Order
class Order(models.Model):
    class OrderStatus(models.TextChoices):  # Alternativ mit IntegerChoices
        UNASSIGNED = "unassigned"
        IN_PROGRESS = "in_progress"
        COOKED = "cooked"
        DELIVERED = "delivered"
        BILLED = "billed"

    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, default=None, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, default=None, null=True)
    chef = models.ForeignKey(Chef, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    timestamp = models.DateTimeField(default=None)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.UNASSIGNED)
    dishId = models.IntegerField(default=-1)
    extraWishes = models.CharField(max_length=250, default=None, blank=True, null=True)

    def info_for_chef(self):
        return '\nStatus: ' + self.get_status_display() + \
               '\nChef: ' + str(self.chef) + \
               '\nDish: ' + str(self.dishId) + \
               '\nExtra wishes: ' + str(self.extraWishes) + \
               '\n\n'

    def info_for_waiter(self):
        return '\nStatus: ' + self.get_status_display() + \
               '\nWaiter: ' + str(self.waiter) + \
               '\nTable Number: ' + str(self.table.tableNumber) + \
               '\nDish: ' + str(self.dishId) + \
               '\nExtra wishes: ' + str(self.extraWishes) + \
               '\n\n'


# Model Reservation
class Reservation(models.Model):
    customerName = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=None, null=True)
    table = models.ManyToManyField(Table)
    places = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "\n\nID: " + str(self.pk) + \
               '\ntimestamp: ' + str(self.timestamp) + \
               '\nplaces: ' + str(self.places) + \
               '\ntable(s): ' + str(self.extractTableNumbers())

    def extractTableNumbers(self):
        # function which extracts only the table numbers from a queryset and returns them as string
        qSet = Reservation.objects.get(pk=self.pk).table.all()  # table.all() gets manytomany values

        stringWithTableNumbers = ''

        for stringItem in qSet:
            stringWithTableNumbers += str([int(num) for num in str(stringItem).split() if num.isdigit()][0])
            stringWithTableNumbers += ', '

        stringWithTableNumbers = stringWithTableNumbers[:-2]

        return stringWithTableNumbers
