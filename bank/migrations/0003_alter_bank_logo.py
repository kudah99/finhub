# Generated by Django 5.0.1 on 2024-04-09 17:09

import app.storage_backend
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_financialservicecategory_bank_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=app.storage_backend.PublicMediaStorage(), upload_to=''),
        ),
    ]
