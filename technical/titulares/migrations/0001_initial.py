# Generated by Django 3.0.7 on 2020-06-03 15:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación')),
                ('cuit', models.IntegerField(unique=True, verbose_name='CUIT')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fisica',
            fields=[
                ('titular_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='titulares.Titular')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=250, verbose_name='Apellido')),
                ('dni', models.IntegerField(verbose_name='Documento Nacional de Identidad')),
            ],
            options={
                'abstract': False,
            },
            bases=('titulares.titular',),
        ),
        migrations.CreateModel(
            name='Juridica',
            fields=[
                ('titular_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='titulares.Titular')),
                ('razonSoc', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('year', models.IntegerField(verbose_name='Año de Fundacion')),
            ],
            options={
                'abstract': False,
            },
            bases=('titulares.titular',),
        ),
    ]
