# Generated by Django 5.1.3 on 2024-11-10 21:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0003_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_id",
        ),
        migrations.RemoveField(
            model_name="order",
            name="tickets",
        ),
        migrations.AddField(
            model_name="nightclub",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="nightclub",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=9, null=True
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="payment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(default="pending", max_length=20),
        ),
    ]
