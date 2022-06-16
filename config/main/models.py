from enum import Enum

from django.db import models


# Model Waiter
class Waiter(models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.surname + ' ' + self.lastname


# Model Chef
class Chef(models.Model):
    surname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.surname + ' ' + self.lastname

# Model Table
class Table(models.Model):
    table_number = models.IntegerField(default=None, null=True)
    places = models.IntegerField(default=None, null=True)

    def __str__(self):
        return '\nTable: ' + self.table_number + '\n\n'


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
    dish_ID = models.IntegerField(default=-1)
    extra_wishes = models.CharField(max_length=250, default=None, blank=True, null=True)

    def info_for_chef(self):
        return '\nStatus: ' + self.get_status_display() + \
               '\nChef: ' + str(self.chef) + \
               '\nDish: ' + str(self.dish_ID) + \
               '\nExtra wishes: ' + str(self.extra_wishes) + \
               '\n\n'

    def info_for_waiter(self):
        return '\nStatus: ' + self.get_status_display() + \
               '\nWaiter: ' + str(self.chef) + \
               '\nTable Number: ' + str(self.table.table_number) + \
               '\nDish: ' + str(self.dish_ID) + \
               '\nExtra wishes: ' + str(self.extra_wishes) + \
               '\n\n'

# Model Reservation
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=None, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    places = models.IntegerField(default=None, null=True)

# es gibt noch statt ForeignKey OneToOne und ManyToMany (brauchen wir das auch???) -> wahrscheinlich ja bei Waiter

# https://ilovedjango.com/django/models-and-databases/foreign-keys-on_delete-option-in-django-models/
# https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
# https://stackoverflow.com/questions/16046478/django-model-nullable-field

# manytomany -> tabelle
# https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
# https://zerotobyte.com/django-many-to-many-relationship-explained/
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_many.html
# https://www.reddit.com/r/django/comments/l937f1/the_right_way_to_use_a_manytomanyfield_in_django/

# query bei abfrage in tests

#textchoices Ausschreiben (get_status_display())
#https://stackoverflow.com/questions/59606682/how-to-get-textchoice-enum-value-in-str-method

#an value von foreign key rankommen:
#self.table.table_number

#wenn man TextChoices hat dann gibt es immer eine methode get_FOO_display() mit der der String von dem Jeweiligen Choice ausgegeben werden kann

#wenn man Objekt ausgeben möchte was eventuell noch nicht belegt ist, dann einfach __str__ Methode definieren (und so belegen
# dass wenn ein Objekt ausgegeben werden soll was schon definiert ist auch sauber aussieht) und dort
#wo man Objekt (none) ausgeben möchte mit str(object) aufrufen