# Generated by Django 4.1.6 on 2023-03-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_book_file_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
