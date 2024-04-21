from django.db import models

# Create your models here.


class DataTable(models.Model):
  id = models.IntegerField(primary_key=True)
  sensor_1=models.IntegerField()
  sensor_2=models.IntegerField()   
  temperature=models.IntegerField()
  humidity=models.IntegerField()
  pump_1=models.BooleanField()
  pump_2=models.BooleanField()
  
  
  


class SettingTable(models.Model):
  id = models.FloatField(primary_key=True)
  minsensor_1=models.FloatField()
  maxsensor_1=models.FloatField()
  minsensor_2=models.FloatField()
  maxsensor_2=models.FloatField()
  plant_1=models.CharField(null=True, blank=True,max_length=100)
  plant_2=models.CharField(null=True, blank=True,max_length=100)
