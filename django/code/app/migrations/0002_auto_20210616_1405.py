# Generated by Django 3.2.4 on 2021-06-16 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience_period', models.CharField(default='', max_length=200)),
                ('skilled', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience_period', models.CharField(default='', max_length=200)),
                ('skilled', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience_period', models.CharField(default='', max_length=200)),
                ('skilled', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience_period', models.CharField(default='', max_length=200)),
                ('skilled', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('experience_period', models.CharField(default='', max_length=200)),
                ('skilled', models.BooleanField(default=False)),
                ('like', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='tool',
            name='experience_period',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(default='')),
                ('introduction', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
