# Generated by Django 3.1.2 on 2020-10-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20201022_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='bandcamp',
            field=models.CharField(max_length=500),
        ),
    ]
