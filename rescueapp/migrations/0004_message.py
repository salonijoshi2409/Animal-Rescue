# Generated by Django 3.1.6 on 2021-05-16 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workwithus', '0002_auto_20210505_2023'),
        ('rescueapp', '0003_auto_20210430_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(default='None', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workwithus.signupclass')),
            ],
        ),
    ]
