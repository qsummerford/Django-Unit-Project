# Generated by Django 3.2.7 on 2021-11-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211109_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
