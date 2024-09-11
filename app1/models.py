from django.db import models

class Register(models.Model):
    fullname=models.CharField(max_length=50,primary_key=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=50)
    phone=models.IntegerField()

def __str__(self):
    return self.email



class Contact_data(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.EmailField(max_length=30,unique=True,primary_key=True)
    phone=models.IntegerField()
    msg=models.CharField(max_length=200)



    