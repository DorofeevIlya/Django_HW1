# Generated by Django 5.0.4 on 2024-04-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1app', '0003_alter_goods_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
