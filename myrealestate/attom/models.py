from django.db import models
# Create your models here.


class Property(models.Model):
    identifier = models.JSONField(default=None, blank=True, null=True)
    lot = models.JSONField(default=None, blank=True, null=True)
    area = models.JSONField(default=None, blank=True, null=True)
    address = models.JSONField(default=None, blank=True, null=True)
    location = models.JSONField(default=None, blank=True, null=True)
    summary = models.JSONField(default=None, blank=True, null=True)
    utilities = models.JSONField(default=None, blank=True, null=True)
    building = models.JSONField(default=None, blank=True, null=True)
    vintage = models.JSONField(default=None, blank=True, null=True)
    property_on_date = models.DateTimeField(auto_now=True)
