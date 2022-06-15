from django.db import models

#Model Waiter
class Waiter(models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.surname + ' ' + self.lastname

#Model Chef
class Chef(models.Model):
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return self.surname + ' ' + self.lastname

#Model Table
class Table(models.Model):
    waiter = models.ForeignKey(Waiter) #??????
    table_number = models.IntegerField()


#Model Order
class Order(models.Model):
    waiter = models.ForeignKey(Waiter)
    chef = models.ForeignKey(Waiter)
    table = models.ForeignKey(Table)
    timestamp = models.DateTimeField()
    cooked = models.BooleanField()
    delivered = models.BooleanField()
    billed = models.BooleanField()
    dish_ID = models.IntegerField()
    extra_wishes = models.CharField(max_length=250)

    def update_cooked(self, status):
        cooked = status

#Model Reservation
class Reservation(models.Model):
    waiter = models.ForeignKey(Waiter)
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    table = models.ForeignKey(Table)

# in Class Customer
#waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE) -> wenn man zugeordneten
# Waiter löscht dann löscht man auch alle Customer die diesen Waiter als Waiter hatten

#es gibt noch statt ForeignKey OneToOne und ManyToMany (brauchen wir das auch???) -> wahrscheinlich ja bei Waiter

#https://ilovedjango.com/django/models-and-databases/foreign-keys-on_delete-option-in-django-models/

