# Generated by Django 3.0.8 on 2020-11-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0004_auto_20201110_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
