# Generated by Django 5.1.1 on 2024-09-16 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_customer_created_at_alter_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 9, 16, 10, 0, 14, 246487)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2024, 9, 16, 10, 0, 14, 246487)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 16, 10, 0, 14, 246487)),
        ),
    ]
