from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class about(models.Model):
    calender = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Documents')
    desc1 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=100)
    about = models.CharField(max_length=100)