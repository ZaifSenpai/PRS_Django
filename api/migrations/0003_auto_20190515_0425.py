# Generated by Django 2.2.1 on 2019-05-14 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190515_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sms',
            name='id',
        ),
        migrations.AlterField(
            model_name='sms',
            name='Sms_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
