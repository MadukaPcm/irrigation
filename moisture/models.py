from django.db import models
from datetime import datetime, timezone

class DataTable(models.Model):
  id = models.IntegerField(primary_key=True)
  sensor_1=models.IntegerField()
  sensor_2=models.IntegerField()   
  temperature=models.IntegerField()
  humidity=models.IntegerField()
  pump_1=models.BooleanField()
  pump_2=models.BooleanField()
  update_at = models.DateTimeField(auto_now=True)
  
  def get_time_dft_in_min(self):
    if not self.update_at.tzinfo:
        self.update_at = self.update_at.astimezone(timezone.utc)

    time_delta = datetime.now(timezone.utc) - self.update_at
    return int(time_delta.total_seconds() / 60)

    # time_delta = datetime.now() - self.update_at
    # return int(time_delta.total_seconds / 60)
  


class SettingTable(models.Model):
  id = models.FloatField(primary_key=True)
  minsensor_1=models.FloatField()
  maxsensor_1=models.FloatField()
  minsensor_2=models.FloatField()
  maxsensor_2=models.FloatField()
  plant_1=models.CharField(null=True, blank=True,max_length=100)
  plant_2=models.CharField(null=True, blank=True,max_length=100)
