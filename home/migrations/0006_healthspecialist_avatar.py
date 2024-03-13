# Generated by Django 5.0.1 on 2024-01-22 12:24

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_medicalspecialty_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthspecialist',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[500, 500], upload_to='medical_specialists/'),
        ),
    ]
