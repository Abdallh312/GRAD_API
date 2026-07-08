from rest_framework import serializers
from .models import delocation

class delocationse(serializers.ModelSerializer):
    class Meta:
        model = delocation
        fields = ('pk','longitude', 'latitude', 'images', 'is_accident', 'is_fire','target_angle','servo_angle','predict','description')