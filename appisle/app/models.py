from django.db import models

# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=200)
    app_link = models.CharField(max_length=500)
    icon_link = models.CharField(max_length=500,default="")
    category = models.CharField(max_length=200,default="")
    sub_category = models.CharField(max_length=200,default="")
    points = models.IntegerField(default=0)