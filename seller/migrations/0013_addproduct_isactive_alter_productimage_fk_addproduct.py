# Generated by Django 5.1.1 on 2024-11-22 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_rename_brand_addproduct_brand1'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='fk_addProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='seller.addproduct'),
        ),
    ]
