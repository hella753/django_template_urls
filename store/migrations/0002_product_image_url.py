# Generated by Django 5.1.2 on 2024-10-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='img', max_length=150, verbose_name='დროებითი სურათი'),
            preserve_default=False,
        ),
    ]
