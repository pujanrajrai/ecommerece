# Generated by Django 3.1.5 on 2021-01-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]