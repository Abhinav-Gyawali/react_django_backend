# Generated by Django 5.1.3 on 2024-11-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_orderitem_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]