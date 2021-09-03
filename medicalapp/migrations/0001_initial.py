# Generated by Django 3.1.5 on 2021-02-22 02:56

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disease', to='medicalapp.disease')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='default.svg', force_format=None, keep_meta=True, quality=0, size=[300, 300], upload_to='doctor_images')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=70)),
                ('division', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('doctors', models.ManyToManyField(to='medicalapp.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='fields',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalapp.field'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='treats',
            field=models.ManyToManyField(to='medicalapp.Disease'),
        ),
    ]