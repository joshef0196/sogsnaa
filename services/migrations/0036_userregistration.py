# Generated by Django 3.1.4 on 2022-07-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0035_employeelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_name', models.CharField(max_length=160)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('designation', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('facebook_id', models.CharField(blank=True, max_length=200)),
                ('twitter_id', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'User Registration',
                'verbose_name_plural': 'User Registration',
            },
        ),
    ]