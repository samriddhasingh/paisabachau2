# Generated by Django 3.2.3 on 2021-06-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gaminglaptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
