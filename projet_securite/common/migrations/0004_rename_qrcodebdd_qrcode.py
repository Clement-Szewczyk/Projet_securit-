# Generated by Django 4.1.5 on 2023-02-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_qrcode_qrcodebdd'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='qrcodebdd',
            new_name='qrcode',
        ),
    ]
