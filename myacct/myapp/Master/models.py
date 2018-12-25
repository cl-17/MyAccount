from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Classification(models.Model):
    ClassificationCode = models.CharField(
        max_length=2,
        primary_key=True,
    )

    ClassificationName = models.TextField(
        default='',
    )

    CreateDate = models.DateTimeField(
        default=timezone.now,
    )

    CreateUser = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING,
        related_name='C_CreateUser',
    )
    
    UpdateDate = models.DateTimeField(
        default=timezone.now
    )

    UpdateUser = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING, 
        related_name='C_UpdateUser'
    )

    def __str__(self):
        return self.ClassificationName


class Purpose(models.Model):
    PurposeCode = models.CharField(
        max_length=4, 
        primary_key=True,
    )

    PurposeName = models.TextField(
        default='',
    )

    ClassificationCode = models.ForeignKey(
        Classification, 
        on_delete=models.DO_NOTHING,
    )

    CreateDate = models.DateTimeField(
        default=timezone.now,
    )

    CreateUser = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING,
        related_name='P_CreateUser',
    )

    UpdateDate = models.DateTimeField(
        default=timezone.now,
    )

    UpdateUser = models.ForeignKey(
        User, 
        on_delete=models.DO_NOTHING, 
        related_name='P_UpdateUser',
    )

    moldel_c = Classification()

    def __str__(self):
        return self.PurposeName

