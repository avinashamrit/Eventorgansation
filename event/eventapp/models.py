from django.db import models
from django.contrib.auth.models import User

#Family
class Family(models.Model):
    Event_Type=models.CharField(max_length=50)
    Desc=models.TextField(max_length=5000)
    Image=models.ImageField(upload_to="Family_images")
    Food=models.CharField(max_length=500)
    Decoration=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')

    
#Charity
class Charity(models.Model):
    Event_Type=models.CharField(max_length=50)
    Desc=models.TextField(max_length=5000)
    Image=models.ImageField(upload_to="Charity_images")
    Food=models.CharField(max_length=50)
    Decoration=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')


# Buisness
class Buisness(models.Model):
    Event_type=models.CharField(max_length=50)
    Desc=models.TextField(max_length=5000)
    Image_name=models.ImageField(upload_to="Buisness_images")
    Food=models.CharField(max_length=50)
    Pubilcity=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')

#Bookevent
class Bookevent(models.Model):
    Name = models.CharField(max_length=50)
    Mobile = models.IntegerField(primary_key=True)
    Location = models.CharField(max_length=150)
    Email = models.EmailField()
    People = models.CharField(max_length=50)
    Date = models.DateField()
    Event = models.CharField(max_length=150)
    Food = models.CharField(max_length=200)
    Address = models.CharField(max_length=1200)
    Message = models.CharField(max_length=1200)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')

#contact us
class Contactus(models.Model):
    Name = models.CharField(max_length=120)
    Mobile = models.IntegerField(primary_key=True)
    Email = models.EmailField(max_length=50)
    Message = models.TextField()

#Culture
class Culture(models.Model):
    Event_Type=models.CharField(max_length=50)
    Desc=models.TextField(max_length=5000)
    Image=models.ImageField(upload_to="Culture_images")
    Food=models.CharField(max_length=50)
    Decoration=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')

