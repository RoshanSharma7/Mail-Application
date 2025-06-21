from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MailUser

@receiver(post_save, sender=User)
def create_mail_user(sender, instance, created, **kwargs):
    if created:
        MailUser.objects.create(user=instance)
