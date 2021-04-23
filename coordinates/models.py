from django.db import models

# Create your models here.

class Message(models.Model):
    vemac_id = models.IntegerField()
    date = models.CharField('Date', max_length=6, blank=True)
    time = models.CharField('Time', max_length=8, blank=True)
    lat = models.CharField('Lat', max_length=10, blank=True)
    lon = models.CharField('Lon', max_length=10, blank=True)
    speed = models.CharField('Speed', max_length=10, blank=True)
    course = models.CharField('Course', max_length=10, blank=True)
    sats = models.CharField('Sats', max_length=10, blank=True)
    danger = models.CharField('Danger', max_length=5, blank=True)
    overlake = models.CharField('Overlake', max_length=1, blank=True)
