# Generated by Django 3.2 on 2021-06-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20210630_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_favourite',
            new_name='is_student',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='phonenum',
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_tutor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='locality',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phn_num',
            field=models.CharField(default='', max_length=12),
        ),
    ]
