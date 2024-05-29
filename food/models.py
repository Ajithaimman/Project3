from django.db import models


class Food(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="images/",null=True,blank=True)


class FoodSharing(models.Model):
    
    fname=models.CharField(max_length=100)
    foodname=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    foodtype=models.CharField(max_length=20,blank=True,null=True)
    

    