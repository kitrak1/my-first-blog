# Generated by Django 2.0.4 on 2018-07-17 19:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
