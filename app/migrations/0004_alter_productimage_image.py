# Generated by Django 5.1.3 on 2024-12-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_product_category_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.BinaryField(),
        ),
    ]
