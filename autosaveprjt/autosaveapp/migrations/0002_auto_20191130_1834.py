# Generated by Django 2.2.6 on 2019-11-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autosaveapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automodel',
            old_name='doc',
            new_name='bike',
        ),
        migrations.RenameField(
            model_name='automodel',
            old_name='nur',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='automodel',
            old_name='patient',
            new_name='lname',
        ),
        migrations.AddField(
            model_name='automodel',
            name='symptoms',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='automodel',
            name='text',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
