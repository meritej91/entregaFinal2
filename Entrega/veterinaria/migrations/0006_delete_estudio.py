# Generated by Django 4.2.5 on 2023-10-12 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0005_remove_turno_edad_remove_turno_raza_turno_apellido_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estudio',
        ),
    ]
