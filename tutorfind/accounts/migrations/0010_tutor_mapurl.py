# Generated by Django 3.2 on 2021-06-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_tutor_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='mapurl',
            field=models.URLField(default=''),
        ),
    ]
