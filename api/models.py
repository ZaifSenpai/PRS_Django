from django.db import models


class Sms(models.Model):
    Sms_ID = models.IntegerField(primary_key=True)
    Sms_ID_Source = models.CharField(max_length=10)
    Address = models.CharField(max_length=20)
    Body = models.TextField()
    Date = models.IntegerField()
    IsProcessed = models.BooleanField(default=False)
    UserId = models.IntegerField(default=0)

class Recommendation(models.Model):
    RecoId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Image = models.URLField()
    Url = models.URLField()
    Price = models.FloatField(default=0.0)


class UserRecommendation(models.Model):
    Id = models.IntegerField(primary_key=True)
    RecoId = models.IntegerField()


class UserInterest(models.Model):
    InterestId = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=20)
    IsSearched = models.BooleanField(default=False)
    RecoId = models.IntegerField(blank=True, null=True)

class Topics(models.Model):
    TopicId = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=20)
    ProcessedDatetime = models.IntegerField()
