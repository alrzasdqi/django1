# Generated by Django 2.2.1 on 2019-05-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
