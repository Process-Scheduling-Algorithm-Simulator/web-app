# Generated by Django 3.1.7 on 2021-03-14 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpualgo',
            old_name='algo_discription',
            new_name='algo_description',
        ),
    ]