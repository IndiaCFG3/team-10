# Generated by Django 3.1 on 2020-08-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_usersignup'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignup',
            name='university',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
