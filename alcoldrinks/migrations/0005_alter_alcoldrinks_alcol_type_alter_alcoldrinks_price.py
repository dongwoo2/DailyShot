# Generated by Django 5.0.7 on 2024-07-20 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcoldrinks', '0004_alcoldrinks_image_alcoldrinks_information_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoldrinks',
            name='alcol_type',
            field=models.CharField(choices=[('Wine', '와인'), ('Whisky', '위스키'), ('Other', '기타'), ('Sake', '사케'), ('Beer', '맥주'), ('Soju', '소주')], default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='alcoldrinks',
            name='price',
            field=models.CharField(max_length=70),
        ),
    ]