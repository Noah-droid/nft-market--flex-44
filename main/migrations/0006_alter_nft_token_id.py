# Generated by Django 4.0.1 on 2022-02-23 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_nft_token_id_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=57953, max_length=5),
        ),
    ]
