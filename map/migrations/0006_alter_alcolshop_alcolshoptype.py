# Generated by Django 5.0.6 on 2024-08-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_alter_alcolshop_alcolshoptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcolshop',
            name='alcolshoptype',
            field=models.CharField(choices=[('store', '스토어'), ('patner', '파트너')], default='patner', max_length=20),
        ),
    ]
