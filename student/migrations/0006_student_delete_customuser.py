# Generated by Django 5.0.1 on 2024-03-10 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('student', '0005_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
