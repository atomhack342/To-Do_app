# Generated by Django 3.2 on 2021-05-26 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='download.jpg', null=True, upload_to='media/images'),
        ),
    ]
