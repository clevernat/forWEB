# Generated by Django 4.0.6 on 2022-07-07 17:43

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('description', models.TextField()),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
