# Generated by Django 4.0.3 on 2022-04-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='isfree',
            field=models.CharField(default='True', max_length=50),
        ),
    ]