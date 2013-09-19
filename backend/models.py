from django.db import models
from django_extensions.db.models import TimeStampedModel
from backend.helpers import DefinedBackends

class Backend(TimeStampedModel):
    backendId=models.AutoField(primary_key=True)
    kind = models.CharField(max_length=20, unique=True,choices=DefinedBackends)
    description = models.CharField(max_length=1000)
    environment=models.CharField(max_length=1000,default='empty')
    script=models.CharField(max_length=1000,default='empty')
    serverIp = models.GenericIPAddressField()
    serverFqdn = models.CharField(max_length=200)
    user=models.CharField(max_length=100,default='root')
    domain=models.CharField(max_length=200,default='linussio.it')


    def __unicode__(self):
        return self.kind
