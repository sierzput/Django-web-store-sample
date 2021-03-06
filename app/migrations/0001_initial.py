# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Ilość')),
            ],
            options={
                'verbose_name': 'Przedmiot w koszyku klienta',
                'verbose_name_plural': 'Przedmioty w koszyku klienta',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=1000, verbose_name='Opis produktu')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cena')),
            ],
            options={
                'verbose_name': 'Przedmiot',
                'verbose_name_plural': 'Przedmioty',
            },
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
