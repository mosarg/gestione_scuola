from django.db import models
from django_extensions.db.models import TimeStampedModel
from sysuser.models import SysUser
from backend.models import Backend
from allocation.models import Role


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
    userId = models.ForeignKey(SysUser)
    backendId = models.ForeignKey(Backend)
    policy = models.ManyToManyField(Policy, through='AssignedPolicy')

    class Meta:
        unique_together = ("userId", "backendId")

    def __unicode__(self):
        return self.username


class AssignedPolicy(TimeStampedModel):
    assignedPolicyId=models.AutoField(primary_key=True)
    accountId = models.ForeignKey(Account)
    policyId = models.ForeignKey(Policy)

    class Meta:
        unique_together = ("accountId", "policyId")