# Generated by Django 5.0.6 on 2024-08-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alcoldrinks', '0008_alter_alcoldrinks_alcol_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoldrinks',
            name='alcol_type',
            field=models.CharField(choices=[('Whisky', '위스키'), ('Soju', '소주'), ('Other', '기타'), ('Sake', '사케'), ('Beer', '맥주'), ('Wine', '와인')], default='Other', max_length=20),
        ),
    ]
