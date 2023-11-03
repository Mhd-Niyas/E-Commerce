from django.db import models

# Create your models here.

class contactusdb(models.Model):
    C_Name = models.CharField(max_length=20,null=True,blank=True)
    C_Email = models.EmailField(max_length=20,null=True,blank=True)
    C_City = models.CharField(max_length=20,null=True,blank=True)
    C_Address = models.CharField(max_length=100,null=True,blank=True)

class registerdb(models.Model):
    R_Name = models.CharField(max_length=20,blank=True,null=True)
    R_Mobile = models.IntegerField(blank=True,null=True)
    R_Email = models.EmailField(max_length=20,blank=True,null=True)
    R_Address = models.CharField(max_length=100,blank=True,null=True)
    R_Username = models.CharField(max_length=20,blank=True,null=True)
    R_Password = models.CharField(max_length=20,blank=True,null=True)

class cartdb(models.Model):
    User_name = models.CharField(max_length=20,blank=True,null=True)
    Product_name = models.CharField(max_length=20,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Quantity = models.IntegerField(blank=True,null=True)
    Total_Price = models.IntegerField(blank=True,null=True)