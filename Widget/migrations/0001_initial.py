# Generated by Django 2.1.5 on 2019-01-29 02:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget', models.CharField(max_length=64)),
                ('packaging', models.CharField(max_length=64)),
                ('customer', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('supplier', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('warehouse', models.CharField(max_length=64)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('minimum_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
