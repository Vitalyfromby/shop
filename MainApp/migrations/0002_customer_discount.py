# Generated by Django 3.0.2 on 2020-02-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='discount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
