# Generated by Django 3.1 on 2020-08-16 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
