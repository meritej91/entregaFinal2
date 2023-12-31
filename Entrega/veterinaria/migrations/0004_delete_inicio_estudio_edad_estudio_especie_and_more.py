# Generated by Django 4.2.5 on 2023-10-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0003_delete_clinica'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inicio',
        ),
        migrations.AddField(
            model_name='estudio',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='estudio',
            name='especie',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='estudio',
            name='nombre',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudio',
            name='raza',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paciente',
            name='especie',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='raza',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='turno',
            name='especie',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='nombre',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='raza',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
