# Generated by Django 4.0.1 on 2022-02-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_bid_date_alter_nft_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=37006, max_length=5),
        ),
    ]
