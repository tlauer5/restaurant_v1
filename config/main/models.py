from django.db import models

#Model Order
class Order(models.Model):
    status_order = models.BooleanField()


