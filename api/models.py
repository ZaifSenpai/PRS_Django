from django.db import models

class Sms(models.Model):
    Sms_ID = models.IntegerField(primary_key=True)
    Sms_ID_Source = models.CharField(max_length=10)
    Address = models.CharField(max_length=20)
    Body = models.TextField()
    Date = models.IntegerField()

class Recommendation(models.Model):
    RecoId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Image = models.URLField()
    Url = models.URLField()
    Price = models.FloatField(default=0.0)
