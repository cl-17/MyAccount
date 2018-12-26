from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Classification(models.Model):
    c_id = models.CharField(
        max_length=2,
        primary_key=True,
    )

    c_name = models.TextField(
        default='',
    )

    c_create_user = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING,
        related_name='c_create_user',
    )

    c_create_date = models.DateTimeField(
        default=timezone.now,
    )

    c_update_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='c_update_user',
    )

    c_update_date = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return self.c_name


class Purpose(models.Model):
    p_id = models.CharField(
        max_length=4,
        primary_key=True,
    )

    p_name = models.TextField(
        default='',
    )

    c_id = models.ForeignKey(
        Classification,
        on_delete=models.DO_NOTHING,
    )

    p_sub_id = models.CharField(
        max_length=2,
        null=False,
    )

    p_create_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='p_create_user',
    )

    p_create_date = models.DateTimeField(
        default=timezone.now,
    )

    p_update_user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='p_update_user',
    )

    p_update_date = models.DateTimeField(
        default=timezone.now,
    )

    moldel_c = Classification()

    def __str__(self):
        return self.p_name

