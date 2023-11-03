from django.db import models

# Create your models here.

class categorydb(models.Model):
    CatName = models.CharField(max_length=50,null=True,blank=True)
    CatDes = models.CharField(max_length=50,null=True,blank=True)
    CatImg = models.ImageField(upload_to="Category Profiles",null=True,blank=True)

class Productdb3(models.Model):
    Select_Product = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="Product Images",null=True,blank=True)