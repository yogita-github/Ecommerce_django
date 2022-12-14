# Generated by Django 4.0.5 on 2022-08-07 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='razorpay_signature_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
