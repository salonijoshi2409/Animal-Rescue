# Generated by Django 3.1.6 on 2021-04-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescueapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescueclass',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]