# Generated by Django 3.0.2 on 2020-04-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_name_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order_num',
            field=models.IntegerField(default=10, verbose_name='Номер п/п'),
        ),
    ]
