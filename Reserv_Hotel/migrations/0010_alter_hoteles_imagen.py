# Generated by Django 5.1.2 on 2024-11-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reserv_Hotel', '0009_hoteles_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoteles',
            name='imagen',
            field=models.ImageField(default=1, upload_to='productos'),
            preserve_default=False,
        ),
    ]