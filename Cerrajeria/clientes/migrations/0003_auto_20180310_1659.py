# Generated by Django 2.0.3 on 2018-03-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20180310_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='Observacion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
