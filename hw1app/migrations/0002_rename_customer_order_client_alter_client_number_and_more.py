# Generated by Django 5.0.4 on 2024-04-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw1app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goods',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
