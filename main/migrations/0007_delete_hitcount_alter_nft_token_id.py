# Generated by Django 4.0.1 on 2022-02-23 14:39

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_merge_20220223_0528'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HitCount',
        ),
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=main.models.random_token, max_length=5),
        ),
    ]
