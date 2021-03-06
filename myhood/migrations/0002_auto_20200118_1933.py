# Generated by Django 2.2.4 on 2020-01-18 16:33

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='b_pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('depart_pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('description', models.TextField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhood.Neighborhood')),
            ],
        ),
    ]
