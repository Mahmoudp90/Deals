# Generated by Django 4.0.4 on 2022-06-30 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_tenders_insurance_money_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='tender',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='tenderer',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='title',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tenderer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tenderer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='tenderer',
            name='user',
        ),
    ]