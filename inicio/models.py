from django.db import models

class Camiseta(models.Model):
    talle = models.CharField(max_length=5)
    modelo =models.CharField(max_length=100)
    club = models.CharField(max_length=50)

def __str__(self):
    return f"Camiseta({self.id})-{self.club} -{self.modelo}-{self.talle}"