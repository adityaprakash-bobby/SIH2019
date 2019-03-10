from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Uploaddata

@receiver(post_save, sender=User)
def create_uploaddata(sender, instance,created, **kwargs):
    if created:
        Uploaddata.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_uploaddata(sender, instance, **kwargs):
    instance.uploaddata.save()