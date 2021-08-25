# Generated by Django 3.2.6 on 2021-08-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210825_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='payment',
            field=models.CharField(default='1', max_length=900),
            preserve_default=False,
        ),
    ]
