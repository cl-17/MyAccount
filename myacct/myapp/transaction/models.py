from django.db import models
from master.models import Classification, Purpose

class Expense(models.Model):

    id = models.IntegerField(
        primary_key=True,
    )

    date = models.DateField(
        auto_now=False,
    )

    purpose = models.ForeignKey(
        Purpose, 
        on_delete=models.PROTECT,
    )

    ammount = models.DecimalField(
        max_digits=8,
        decimal_places=0,
    )

    credit = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.id

    def display(self):
        return self.id



class Income(models.Model):

    id = models.IntegerField(
        primary_key=True,
    )

    date = models.DateField(
        auto_now=False,
    )

    ammount = models.DecimalField(
        max_digits=8,
        decimal_places=0,
    )

    def __str__(self):
        return self.id

    def display(self):
        return self.id


