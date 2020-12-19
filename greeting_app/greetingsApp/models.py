from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True,db_index=True,)

 

    def __str__(self):
        return self.name
