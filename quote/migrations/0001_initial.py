# Generated by Django 3.1 on 2020-08-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('luggage_type', models.CharField(max_length=50)),
                ('luggage_weight', models.CharField(max_length=20)),
                ('luggage_dimensions', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('mode', models.CharField(max_length=100)),
                ('complete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
