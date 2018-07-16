from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)