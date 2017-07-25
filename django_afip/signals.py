from django.db.models.signals import pre_save
from django.dispatch import receiver

from django_afip import models


@receiver(pre_save, sender=models.TaxPayer)
def update_certificate_expiration(sender, instance, **kwargs):
    if instance.certificate:
        instance.certificate_expiration = instance.get_certificate_expiration()