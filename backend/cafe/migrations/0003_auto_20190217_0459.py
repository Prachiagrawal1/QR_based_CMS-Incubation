# Generated by Django 2.1.7 on 2019-02-17 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_order_order_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='delivered',
        ),
    ]
