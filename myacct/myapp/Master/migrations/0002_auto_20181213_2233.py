# Generated by Django 2.1.3 on 2018-12-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='id',
        ),
        migrations.AlterField(
            model_name='classification',
            name='ClassificationCode',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
