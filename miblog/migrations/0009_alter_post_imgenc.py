# Generated by Django 4.1.3 on 2023-01-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miblog', '0008_post_imgenc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgenc',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]