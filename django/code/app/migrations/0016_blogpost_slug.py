# Generated by Django 3.2.4 on 2021-08-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210801_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
