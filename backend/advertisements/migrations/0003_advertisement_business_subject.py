# Generated by Django 5.1.3 on 2024-11-16 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_client_name_client_surname'),
        ('advertisements', '0002_alter_advertisement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='business_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.businesssubject'),
        ),
    ]
