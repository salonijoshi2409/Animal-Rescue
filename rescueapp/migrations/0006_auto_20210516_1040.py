# Generated by Django 3.1.6 on 2021-05-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescueapp', '0005_auto_20210516_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg',
            field=models.CharField(default='None', max_length=500),
        ),
    ]
