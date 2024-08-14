# Generated by Django 5.0.6 on 2024-07-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_allshop_alcolshoptype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopdrinks_count',
            old_name='drinks',
            new_name='drinks_id',
        ),
        migrations.AlterField(
            model_name='allshop',
            name='alcolshoptype',
            field=models.CharField(choices=[('patner', '파트너'), ('store', '스토어')], default='patner', max_length=20),
        ),
    ]