# Generated by Django 3.2.12 on 2022-09-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=10)),
                ('plan', models.TextField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
