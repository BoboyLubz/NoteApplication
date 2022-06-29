from django.db import models

# Create your models here.
class Register(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email= models.CharField(max_length=40)
    password = models.CharField(max_length=12)
    class Meta:
        db_table = "register"