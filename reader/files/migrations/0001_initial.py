# Generated by Django 4.1.6 on 2023-02-23 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('image_preview', models.ImageField(blank=True, null=True, upload_to='files')),
            ],
        ),
    ]
