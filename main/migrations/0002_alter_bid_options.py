# Generated by Django 4.0.1 on 2022-02-24 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ('-bidprice',)},
        ),
    ]
