# Generated by Django 4.1.1 on 2022-09-14 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_shippingdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='TrackingNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(max_length=12, unique=True)),
                ('status', models.CharField(choices=[('R', 'Item is ready to be dispatched.'), ('P', 'Carrier picked up the package.'), ('D', 'Package arrived at a carrier facility.'), ('O', 'Out for delivery.'), ('U', 'Carrier is unable to gain access to the front door. Please contact Estorage to provide additional information'), ('D', 'Carrier delivered the package.')], default='R', max_length=1)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
