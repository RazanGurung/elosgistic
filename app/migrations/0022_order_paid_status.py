# Generated by Django 4.0.4 on 2022-05-31 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid_status',
            field=models.BooleanField(default=False),
        ),
    ]