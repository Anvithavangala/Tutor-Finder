# Generated by Django 3.2 on 2021-06-28 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='tut',
        ),
    ]