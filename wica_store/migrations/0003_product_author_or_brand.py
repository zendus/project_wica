# Generated by Django 3.2.7 on 2021-09-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wica_store', '0002_product_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author_or_brand',
            field=models.CharField(max_length=100, null=True),
        ),
    ]