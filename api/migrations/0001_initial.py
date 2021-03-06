# Generated by Django 4.0.4 on 2022-05-23 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pdf_tech', models.FileField(upload_to='pdf_tech/')),
                ('pdf_money', models.FileField(upload_to='pdf_money/')),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tenderer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tenders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('pdf_tender', models.FileField(upload_to='pdf_tender/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('endate', models.DateTimeField(default=django.utils.timezone.now)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bidder')),
                ('tenderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tenderer')),
            ],
        ),
        migrations.CreateModel(
            name='Mydeals_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bid')),
                ('tender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tenders')),
                ('tenderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tenderer')),
            ],
        ),
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bidder'),
        ),
        migrations.AddField(
            model_name='bid',
            name='tender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tenders'),
        ),
        migrations.AddField(
            model_name='bid',
            name='tenderer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tenderer'),
        ),
    ]
