from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    JINS_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    jins = models.CharField(max_length=10, )
    rasm = models.ImageField(upload_to='users/')
    manzil = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
