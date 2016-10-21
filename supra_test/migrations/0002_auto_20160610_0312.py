# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 08:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supra_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyInlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=45)),
                ('field2', models.CharField(max_length=45)),
                ('field3', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='field3',
            field=models.ImageField(upload_to=b'image'),
        ),
        migrations.AddField(
            model_name='myinlinemodel',
            name='mymodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supra_test.MyModel'),
        ),
    ]