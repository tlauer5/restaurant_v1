from enum import Enum

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
        #function which extracts only the table numbers from a queryset and returns them as string
        qSet = Reservation.objects.get(pk=self.pk).table.all() #table.all() gets manytomany values

        stringWithTableNumbers = ''

        for stringItem in qSet:
            stringWithTableNumbers += str([int(num) for num in str(stringItem).split() if num.isdigit()][0])
            stringWithTableNumbers += ', '

        stringWithTableNumbers = stringWithTableNumbers[:-2]

        return stringWithTableNumbers




# es gibt noch statt ForeignKey OneToOne und ManyToMany (brauchen wir das auch???) -> wahrscheinlich ja bei Waiter

# https://ilovedjango.com/django/models-and-databases/foreign-keys-on_delete-option-in-django-models/
# https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
# https://stackoverflow.com/questions/16046478/django-model-nullable-field
# https://stackoverflow.com/questions/7655438/how-do-django-fixtures-handle-manytomanyfields

# manytomany
# reservations auf table ist manytomany -> dann muss man alle table in reservations.json als Liste angeben []
# ein table kann schon allein mit foreign key mehrere reservations haben... aber eine reservation bisher nur ein tisch
# mit manytomanyfield(table) -> k??nnen beide Objekte in beide Richtungen mehrere Objekte haben
# https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
# https://zerotobyte.com/django-many-to-many-relationship-explained/
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_many.html
# https://www.reddit.com/r/django/comments/l937f1/the_right_way_to_use_a_manytomanyfield_in_django/

# query bei abfrage in tests

#textchoices Ausschreiben (get_status_display())
#https://stackoverflow.com/questions/59606682/how-to-get-textchoice-enum-value-in-str-method

#an value von foreign key rankommen:
#self.table.tableNumber

#wenn man TextChoices hat dann gibt es immer eine methode get_FOO_display() mit der der String von dem Jeweiligen Choice ausgegeben werden kann

#wenn man Objekt ausgeben m??chte was eventuell noch nicht belegt ist, dann einfach __str__ Methode definieren (und so belegen
# dass wenn ein Objekt ausgegeben werden soll was schon definiert ist auch sauber aussieht) und dort
#wo man Objekt (none) ausgeben m??chte mit str(object) aufrufen