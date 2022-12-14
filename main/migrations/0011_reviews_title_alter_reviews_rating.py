# Generated by Django 4.1 on 2022-09-09 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_book_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
