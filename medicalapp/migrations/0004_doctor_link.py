# Generated by Django 3.1.5 on 2021-02-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0003_auto_20210222_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
