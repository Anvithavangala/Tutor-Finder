# Generated by Django 3.2 on 2021-06-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tutor_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]