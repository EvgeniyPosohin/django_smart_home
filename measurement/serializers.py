from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", required=True, read_only=False)
        fields = ['sensor', 'temp', 'data']


class MeasurementsSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temp', 'data']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSensorSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']