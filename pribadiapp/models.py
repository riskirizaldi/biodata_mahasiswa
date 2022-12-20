from django.db import models


class mahasiswa(models.Model):
    name = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    tanggal_lahir = models.CharField(max_length=50)
    
    def __str__(self):
       return self.name
