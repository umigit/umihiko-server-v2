# Generated by Django 3.2.4 on 2021-08-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
    ]
