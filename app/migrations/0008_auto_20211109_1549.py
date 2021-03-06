# Generated by Django 3.2.7 on 2021-11-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_show_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=50, null=True)),
                ('password2', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='email',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='username',
        ),
    ]
