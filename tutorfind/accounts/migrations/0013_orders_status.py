# Generated by Django 3.2.4 on 2021-06-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210626_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(default='', max_length=255),
        ),
    ]
