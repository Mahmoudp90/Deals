# Generated by Django 4.0.4 on 2022-05-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidderslist',
            name='Bidder',
        ),
        migrations.DeleteModel(
            name='mydeals_tenderer',
        ),
        migrations.DeleteModel(
            name='Bidderslist',
        ),
    ]