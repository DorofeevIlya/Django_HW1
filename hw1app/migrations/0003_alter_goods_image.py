# Generated by Django 5.0.4 on 2024-04-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1app', '0002_goods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=None, upload_to=''),
        ),
    ]
