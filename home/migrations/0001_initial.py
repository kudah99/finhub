# Generated by Django 5.0.1 on 2024-04-17 23:54

import app.storage_backend
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, storage=app.storage_backend.PublicMediaStorage(), upload_to='')),
            ],
        ),
    ]
