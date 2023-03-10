# Generated by Django 4.1.6 on 2023-02-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, storage='books', upload_to=''),
        ),
    ]
