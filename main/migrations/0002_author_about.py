# Generated by Django 4.1 on 2022-09-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
