# Generated by Django 5.1.2 on 2024-12-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0009_rename_picture_field_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='field',
            name='type_of_sport',
        ),
        migrations.AddField(
            model_name='field',
            name='sports',
            field=models.ManyToManyField(related_name='fields', to='fields.sport'),
        ),
    ]
