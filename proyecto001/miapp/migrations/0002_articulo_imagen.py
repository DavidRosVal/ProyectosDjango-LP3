# Generated by Django 3.0.8 on 2023-06-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
