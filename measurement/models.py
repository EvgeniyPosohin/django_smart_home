from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.description}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temp = models.DecimalField(decimal_places=2, max_digits=5)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sensor}, {self.temp}, {self.data}'
