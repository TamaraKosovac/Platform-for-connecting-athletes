# Generated by Django 5.1.2 on 2024-12-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0010_sport_remove_field_type_of_sport_field_sports'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='precise_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
