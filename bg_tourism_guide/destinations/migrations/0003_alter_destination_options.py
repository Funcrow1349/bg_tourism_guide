# Generated by Django 4.2.3 on 2023-07-27 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_alter_destination_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
