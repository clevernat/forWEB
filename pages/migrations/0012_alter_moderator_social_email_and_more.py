# Generated by Django 4.0.6 on 2022-07-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_moderator_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='social_email',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_facebook',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_github',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_instagram',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_linkedin',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_snapchat',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_website',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='social_youtube',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]