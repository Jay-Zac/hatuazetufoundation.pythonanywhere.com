# Generated by Django 5.0.2 on 2024-03-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_blog_content_alter_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='url',
            new_name='thumbnail_url',
        ),
    ]
