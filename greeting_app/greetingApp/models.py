from django.db import models

class Index(models.Model):
    name = models.TextField()
    age = models.TextField()
    msg = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
