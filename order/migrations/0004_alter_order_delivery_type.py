# Generated by Django 4.2.2 on 2023-07-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_ordertype_cargotype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('quick', 'qucik'), ('slow', 'slow')]),
        ),
    ]
