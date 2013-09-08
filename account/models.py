from django.db import models
from django_extensions.db.models import TimeStampedModel
from sysuser.models import SysUser
from backend.models import Backend
from account.tasks.generic import runFabricTask


class Policy(TimeStampedModel):
    policyId=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    backendId = models.ForeignKey(Backend)

    class Meta:
        unique_together = ("name", "backendId")

    def __unicode__(self):
        return self.name



class Account(TimeStampedModel):
    accountId=models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    backendUidNumber = models.IntegerField(default=0)
    userId = models.ForeignKey(SysUser,related_name='accounts')
    backendId = models.ForeignKey(Backend,related_name='accounts')
    policy = models.ManyToManyField(Policy, through='AssignedPolicy')


    class Meta:
        unique_together = ("userId", "backendId")

    def __unicode__(self):
        return self.username
#
    def changeBackendPassword(self, password):
        backend=self.backendId.kind
        runFabricTask.delay('account.tasks.'+backend,'passwd','root@'+self.backendId.serverFqdn, self.username, password)
        pass





class AssignedPolicy(TimeStampedModel):
    assignedPolicyId=models.AutoField(primary_key=True)
    accountId = models.ForeignKey(Account)
    policyId = models.ForeignKey(Policy)

    class Meta:
        unique_together = ("accountId", "policyId")