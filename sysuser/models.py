from django.db import models
from django_extensions.db.models import TimeStampedModel



class SysUser(TimeStampedModel):
    userId=models.AutoField(primary_key=True)
    sidiId = models.PositiveIntegerField(unique=True,default=0)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    origin = models.CharField(max_length=45, default='automatic')
    insertOrder = models.IntegerField(default=0)
    syncModel=models.CharField(max_length=30,default='sync')

    def __unicode__(self):
        return self.name+' '+self.surname
