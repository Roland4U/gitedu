# Generated by Django 3.1.5 on 2021-01-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitedu', '0007_ordertoserv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertoserv',
            name='text',
            field=models.TextField(max_length=900),
        ),
    ]
