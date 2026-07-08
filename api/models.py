from django.db import models
from datetime import datetime
# Create your models here.
#delocation store longitude,latitude,images,is_accident,is_fire,servo_angle,target_angle,predict

class delocation(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    images = models.TextField(max_length=1000000000000000000000000,default="")
    is_accident = models.BooleanField()
    is_fire = models.BooleanField()
    servo_angle=models.FloatField(default=0)
    target_angle=models.FloatField(default=0)
    predict=models.BooleanField(default=False)
    description = models.TextField(max_length=1000000000000000000000000, default="")
    def __str__(self):
        return f"({self.longitude}, {self.latitude})"