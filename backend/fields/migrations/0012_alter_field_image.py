# Generated by Django 5.1.2 on 2024-12-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0011_field_precise_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./media/'),
        ),
    ]
