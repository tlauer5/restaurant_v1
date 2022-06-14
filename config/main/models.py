from django.db import models

#Model Order
class Order(models.Model):
    status_order = models.BooleanField()

#Model Waiter
class Waiter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Model Customer
class Customer(models.Model):
    billed = models.BooleanField()
    waiter = models.ForeignKey(Waiter)




# in Class Customer
#waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE) -> wenn man zugeordneten
# Waiter löscht dann löscht man auch alle Customer die diesen Waiter als Waiter hatten

#es gibt noch statt ForeignKey OneToOne und ManyToMany (brauchen wir das auch???) -> wahrscheinlich ja bei Waiter

#https://ilovedjango.com/django/models-and-databases/foreign-keys-on_delete-option-in-django-models/

