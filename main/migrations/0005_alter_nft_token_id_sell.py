# Generated by Django 4.0.1 on 2022-02-23 00:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_nft_token_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='token_id',
            field=models.IntegerField(default=20794, max_length=5),
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_ends', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('minbidprice', models.DecimalField(decimal_places=3, max_digits=8)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nft')),
            ],
        ),
    ]
