# Generated by Django 4.2.3 on 2023-08-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]
