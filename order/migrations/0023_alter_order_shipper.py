# Generated by Django 4.2.3 on 2023-07-07 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0001_initial'),
        ('order', '0022_alter_order_delivery_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipper.shipper'),
        ),
    ]
