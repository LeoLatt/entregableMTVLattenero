from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre= models.CharField(max_length=22)
    edad= models.IntegerField()
    nacimiento= models.DateField()

    def __str__(self):
        return self.nombre+" "+str(self.edad)+" "+str(self.nacimiento) 