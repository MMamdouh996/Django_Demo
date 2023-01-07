from django.db import models

# Create your models here.

class Trip(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    nights = models.IntegerField()
    price = models.IntegerField()
    model = models.TextField(default="helloXX")
    
    
class Car(models.Model):
    choice=[("123","2013"),("2014","444444"),("2015","2015"),("2016","2016"),]
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d',null=True,blank=True)
    descreption = models.TextField(max_length=500)
    model = models.TextField(default="hello",choices=choice)
    def __str__(self):
        return self.name
    class Meta:
        ordering =["-name"]
        verbose_name = "My Car"

    