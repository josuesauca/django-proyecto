# Generated by Django 4.2.6 on 2023-10-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrador", "0002_alter_tarjeta_numtarjeta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarjeta",
            name="numTarjeta",
            field=models.IntegerField(null=True),
        ),
    ]
