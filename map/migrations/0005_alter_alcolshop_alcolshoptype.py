# Generated by Django 5.0.6 on 2024-07-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_alter_alcolshop_alcolshoptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcolshop',
            name='alcolshoptype',
            field=models.CharField(choices=[('patner', '파트너'), ('store', '스토어')], default='patner', max_length=20),
        ),
    ]