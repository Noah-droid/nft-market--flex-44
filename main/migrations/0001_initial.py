# Generated by Django 4.0.1 on 2022-02-15 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('nft_id', models.AutoField(primary_key=True, serialize=False)),
                ('nft_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('nft_image', models.ImageField(upload_to='nftpictures')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='NFT_Collection',
            fields=[
                ('nft_collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_name', models.CharField(max_length=30)),
                ('creator', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='nftpictures')),
                ('description', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
            ],
        ),
        migrations.CreateModel(
            name='Nft_Bid',
            fields=[
                ('nft_bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('bidder_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
                ('nft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nft')),
            ],
        ),
        migrations.AddField(
            model_name='nft',
            name='collection_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nft_collection'),
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.wallet'),
        ),
    ]
