# Generated by Django 4.0.4 on 2022-06-05 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_bidder_insurance_money_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenders',
            name='endate',
        ),
        migrations.AlterField(
            model_name='tenders',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='tenders',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
