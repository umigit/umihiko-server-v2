# Generated by Django 3.2.4 on 2021-08-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_blogpost_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
