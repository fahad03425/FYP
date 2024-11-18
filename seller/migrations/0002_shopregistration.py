# Generated by Django 5.1.1 on 2024-10-25 18:24

import django.db.models.deletion
import django.utils.timezone
import seller.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_customuser_isseller'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopID', models.IntegerField(default=seller.models.generate_shop_id)),
                ('shopname', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('area', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='marketplace.customuser')),
            ],
        ),
    ]
