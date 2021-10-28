from django.db import models

# Create your models here.


class Route(models.Model):
    fin = models.CharField(max_length=100)
    via = models.CharField(max_length=500)
    etc = models.TextField()

    def __str__(self):
        return self.fin
