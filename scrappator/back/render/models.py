from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

class Search(models.Model):
    searchbar = models.CharField(max_length=500)


