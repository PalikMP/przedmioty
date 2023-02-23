from django.db import models

# Create your models here.
class Rowery(models.Model):
    kogo = models.CharField(max_length=128)
    opis = models.CharField(max_length=500)

    def __str__(self):
        return self.kogo
