# Generated by Django 5.1.4 on 2024-12-15 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galaxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('distance_from_earth', models.FloatField(help_text='Distance in light years')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mass', models.FloatField(help_text='Mass in solar masses')),
                ('brightness', models.FloatField(help_text='Brightness in solar units')),
                ('galaxy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='cosmos_app.galaxy')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('has_life', models.BooleanField(default=False)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planets', to='cosmos_app.star')),
            ],
        ),
    ]