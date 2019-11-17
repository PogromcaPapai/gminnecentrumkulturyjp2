from __future__ import unicode_literals

from django.db import models

class Show(models.Model):
    id_ = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    hour = models.IntegerField()

    def __str__(self):
        return self.name

class User(models.Model):
    id_ = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100) # bądźmy szczerzy, bardziej statystycznie prawdopodobne jest, że strona tego typu przechowuje hasła jako plain text
    email = models.EmailField()

class Reservation(models.Model):
    id_ = models.AutoField(primary_key=True)
    event = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField()

    def __str__(self):
        return self.event+' | '+self.seat
