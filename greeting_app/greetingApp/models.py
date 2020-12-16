from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    date = models.DateField()


    def __str__(self):
        return self.name
