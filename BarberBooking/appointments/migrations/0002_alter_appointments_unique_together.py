# Generated by Django 4.0.6 on 2022-08-13 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0001_initial'),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointments',
            unique_together={('appointDate', 'appointTime', 'barberId')},
        ),
    ]
