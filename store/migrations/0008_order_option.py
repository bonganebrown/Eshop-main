# Generated by Django 4.2.2 on 2023-07-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='option',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]