# Generated by Django 5.0.2 on 2024-03-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_blog_content_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(),
        ),
    ]