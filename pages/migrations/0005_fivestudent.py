# Generated by Django 4.0.6 on 2022-07-07 20:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_whatwedo_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiveStudent',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('school_and_level', models.CharField(max_length=500)),
                ('interest', models.CharField(max_length=6000, null=True)),
                ('featured_image', models.ImageField(default='five-students/default.jpg', null=True, upload_to='five-students/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
