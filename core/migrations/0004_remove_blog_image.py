# Generated by Django 5.0.2 on 2024-03-10 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]