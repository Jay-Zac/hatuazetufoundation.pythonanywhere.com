# Generated by Django 5.0.2 on 2024-06-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_url_blog_thumbnail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
    ]
