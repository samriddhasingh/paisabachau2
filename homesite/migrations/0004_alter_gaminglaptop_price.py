# Generated by Django 3.2.3 on 2021-06-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0003_auto_20210612_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gaminglaptop',
            name='price',
            field=models.IntegerField(default=123),
        ),
    ]
