# Generated by Django 4.1.6 on 2023-03-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_book_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='content/books'),
        ),
        migrations.AlterField(
            model_name='bookupcoming',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='content/books'),
        ),
    ]
