# Generated by Django 2.2.6 on 2019-10-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slampoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.SlugField(max_length=30),
        ),
    ]