# Generated by Django 4.0.4 on 2022-05-30 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_productimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='name',
        ),
    ]
