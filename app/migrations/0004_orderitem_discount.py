# Generated by Django 5.1.3 on 2024-11-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]