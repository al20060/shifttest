# Generated by Django 4.0.5 on 2022-06-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indiinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('indivisual_ID', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=9)),
                ('status', models.BooleanField()),
                ('store_ID', models.IntegerField()),
            ],
        ),
    ]
