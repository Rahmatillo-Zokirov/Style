from django.db import models

from mainApp.models import Mahsulot
from userApp.models import User


class Savat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} savati"


class SavatMahsulot(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    sana = models.DateTimeField(auto_now_add=True)