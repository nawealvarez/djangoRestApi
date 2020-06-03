from django.utils import timezone

from django.db.models import Model, DateTimeField


class Audit(Model):
    class Meta:
        abstract = True

    create_date = DateTimeField(default=timezone.now, verbose_name='Fecha de creación')
