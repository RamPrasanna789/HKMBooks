# Generated by Django 3.2.6 on 2021-08-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210825_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(default='Razorpay', max_length=200),
        ),
    ]