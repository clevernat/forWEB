# Generated by Django 4.0.6 on 2022-07-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_fivestudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fivestudent',
            name='interest',
            field=models.CharField(blank=True, max_length=6000, null=True),
        ),
    ]
