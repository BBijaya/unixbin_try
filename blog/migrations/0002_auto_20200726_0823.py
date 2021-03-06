# Generated by Django 3.0.3 on 2020-07-26 08:23

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, help_text='seo friendly title for the post', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(help_text='image for the thubnail fo the post (required)', upload_to=blog.models.upload_location),
        ),
    ]
