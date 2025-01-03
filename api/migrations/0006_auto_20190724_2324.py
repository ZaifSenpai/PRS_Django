# Generated by Django 2.2.1 on 2019-07-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_recommendation_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('InterestId', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=20)),
                ('IsSearched', models.BooleanField(default=False)),
                ('RecoId', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRecommendation',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('RecoId', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sms',
            name='IsProcessed',
            field=models.BooleanField(default=False),
        ),
    ]
