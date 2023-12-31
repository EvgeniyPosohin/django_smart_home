# Generated by Django 4.2.4 on 2023-08-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sensor_id', to='measurement.sensor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
