from django.db import models
from django.contrib.auth.models import User

############################################################################

class Classification(models.Model):
    id = models.CharField(
        max_length=2,
        primary_key=True,
    )

    name = models.TextField(
        default='',
    )

    create_user = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='c_create_user',
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
    )

    update_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='c_update_user',
    )

    update_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def display(self):
        return self.id + '：' + self.name

############################################################################

class Purpose(models.Model):
    id = models.CharField(
        max_length=4,
        primary_key=True,
    )

    name = models.TextField(
        default='',
    )

    classification = models.ForeignKey(
        Classification,
        on_delete=models.PROTECT,
    )

    sub_id = models.CharField(
        max_length=2,
        null=False,
    )

    create_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='p_create_user',
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
    )

    update_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='p_update_user',
    )

    update_date = models.DateTimeField(
        auto_now=True,
    )

    moldel_c = Classification()

    def __str__(self):
        return self.name

    def display(self):
        return self.id + '：' + self.name

############################################################################


