from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='bolimlar/')

    def __str__(self):
        return self.nom


class IchkiBolim(models.Model):
    nom = models.CharField(max_length=255)
    rasm = models.ImageField(upload_to='ichki-bolimlar/')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    ichki_bolim = models.ForeignKey(IchkiBolim, on_delete=models.CASCADE)
    batafsil = models.TextField(blank=True, null=True)
    narx = models.FloatField(validators=[MinValueValidator(0)])
    chegirma = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True
    )
    kafolat = models.CharField(max_length=50, blank=True, null=True)
    yetkazish = models.CharField(max_length=50, blank=True, null=True)
    mavjud = models.BooleanField(default=True)
    baho = models.PositiveSmallIntegerField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    korish = models.PositiveSmallIntegerField(default=0)
    buyurtma_soni = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nom


class Rasm(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='mahsulotlar/')

    def __str__(self):
        return self.mahsulot.nom


class Xususiyat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    qiymat = models.CharField(max_length=40)

    def __str__(self):
        return self.nom
