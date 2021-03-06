# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_i_n', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.PositiveIntegerField()),
                ('miejscowosc', models.CharField(max_length=150)),
                ('rodzaj_nier', models.CharField(blank=True, choices=[('M', 'Mieszkanie'), ('D', 'Dom'), ('P', 'Dzia\u0142ka'), ('I', 'Inne')], max_length=1)),
                ('uwagi', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['i_i_n'],
            },
        ),
    ]
