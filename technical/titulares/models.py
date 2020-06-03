from django.db.models import CharField, IntegerField
from technical.audit.models import Audit


class Titular(Audit):
    cuit = IntegerField(verbose_name='CUIT', unique=True)

    def __str__(self):
        return self.cuit


class Fisica(Titular):
    name = CharField(max_length=80, verbose_name='Nombre')
    lastname = CharField(max_length=250, verbose_name='Apellido')
    dni = IntegerField(verbose_name='Documento Nacional de Identidad')

    def __str__(self):
        return self.name


class Juridica(Titular):
    razonSoc = CharField(max_length=100, verbose_name='Razon Social')
    year = IntegerField(verbose_name='Año de Fundacion')

    def __str__(self):
        return self.razonSoc
