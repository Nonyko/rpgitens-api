# Generated by Django 2.2.4 on 2019-08-27 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='common',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='exotic',
            field=models.BooleanField(default=False),
        ),
    ]