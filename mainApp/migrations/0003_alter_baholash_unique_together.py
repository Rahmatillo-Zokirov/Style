# Generated by Django 5.0.6 on 2024-05-21 05:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_baholash'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='baholash',
            unique_together={('mahsulot', 'user')},
        ),
    ]
