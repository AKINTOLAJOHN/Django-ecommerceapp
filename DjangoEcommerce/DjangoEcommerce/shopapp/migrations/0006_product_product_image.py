# Generated by Django 4.0.5 on 2022-07-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_rename_item_validation_product_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_image/'),
        ),
    ]