from django.db import models
from django.utils import timezone

# Create your models here.
class Classification(models.Model):
    ClassificationCode = models.CharField(max_length=2)
    ClassificationName = models.TextField(default='')
    CreateDate = models.DateTimeField(default=timezone.now)
    CreateUser = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, related_name='CreateUser')
    UpdateDate = models.DateTimeField(default=timezone.now)
    UpdateUser = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, related_name='UpdateUser')

    def __str__(self):
        return self.ClassificationName





