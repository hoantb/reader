# Generated by Django 4.1.6 on 2023-03-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_image_preview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='bookupcoming',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
    ]
