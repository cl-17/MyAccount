# Generated by Django 2.1.3 on 2018-12-03 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassificationCode', models.CharField(max_length=2)),
                ('ClassificationName', models.TextField(default='')),
                ('CreateDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('UpdateDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('CreateUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='CreateUser', to=settings.AUTH_USER_MODEL)),
                ('UpdateUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='UpdateUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]