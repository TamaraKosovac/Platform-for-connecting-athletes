# Generated by Django 5.1.2 on 2024-12-07 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0005_alter_advertisement_date'),
        ('fields', '0011_field_precise_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fields.sport'),
        ),
    ]
