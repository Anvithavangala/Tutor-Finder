# Generated by Django 3.2 on 2021-06-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_rename_review_review_tut'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='day',
            field=models.CharField(default='', max_length=255),
        ),
    ]