from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.views import Token

class phone(models.Model):
    brand= models.CharField(max_length=30)
    processor= models.CharField(max_length=30)
    ram= models.IntegerField()
    storage= models.IntegerField()
    def __str__(self):
        return f'{self.brand}'
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)