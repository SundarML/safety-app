# Generated by Django 3.2 on 2022-06-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipments',
            fields=[
                ('eqp_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='equipment id')),
                ('eqp_name', models.CharField(max_length=30, verbose_name='equipment name')),
                ('department', models.CharField(max_length=30, verbose_name='equipment department')),
            ],
        ),
    ]
