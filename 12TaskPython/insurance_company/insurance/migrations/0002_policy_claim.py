# Generated by Django 5.1.3 on 2024-11-25 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=20, unique=True)),
                ('policy_type', models.CharField(choices=[('Auto', 'Автострахование'), ('Health', 'Медицинская страховка'), ('Property', 'Страхование недвижимости')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.client')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=20)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.policy')),
            ],
        ),
    ]
