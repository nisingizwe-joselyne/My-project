# Generated by Django 3.1.6 on 2021-02-12 10:35

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
            name='Cooperativesreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('leadername', models.CharField(max_length=255)),
                ('leaderphone', models.CharField(max_length=255)),
                ('harvesttype', models.CharField(max_length=255)),
                ('Cooperativedistrict', models.CharField(max_length=255)),
                ('Cooperativesector', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Regfarmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('dateofbirth', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('regCooperative', models.CharField(max_length=255)),
                ('farmercode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('Cell', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profilecooperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Instute cooperative Logo')),
                ('cooperativename', models.CharField(max_length=255)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Harvestrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=255)),
                ('farmercode', models.CharField(max_length=255)),
                ('donedate', models.DateField(auto_now=True)),
                ('donetime', models.TimeField(auto_now=True)),
                ('usered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.regfarmer')),
            ],
        ),
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('harvesttype', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
