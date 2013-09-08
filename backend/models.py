from django.db import models
from django_extensions.db.models import TimeStampedModel
from backend.helpers import DefinedBackends

class Backend(TimeStampedModel):
    backendId=models.AutoField(primary_key=True)
    kind = models.CharField(max_length=20, unique=True,choices=DefinedBackends)
    description = models.CharField(max_length=1000)
    serverIp = models.GenericIPAddressField()
    serverFqdn = models.CharField(max_length=200)


    def __unicode__(self):
        return self.kind
