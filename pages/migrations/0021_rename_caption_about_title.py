# Generated by Django 4.0.6 on 2022-07-17 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_rename_title_about_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='caption',
            new_name='title',
        ),
    ]