# Generated by Django 3.2.4 on 2021-06-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_profileen_englishprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='locale',
            field=models.CharField(default='ja', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EnglishProfile',
        ),
    ]