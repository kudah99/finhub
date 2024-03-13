
from django.db import migrations, models
import django.db.models.deletion
from django_resized import ResizedImageField

class Migration(migrations.Migration):

    dependencies = [
        # If this is your first migration, it would likely depend on the initial migration of the app.
        # ('your_app_name', '0003_some_previous_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coarse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', ResizedImageField(size=[500, 300], upload_to='images/', null=True, quality=75, force_format='JPEG')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
