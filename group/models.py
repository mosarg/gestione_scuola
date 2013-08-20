from django.db import models
from django_extensions.db.models import TimeStampedModel
from account.models import Policy

# Create your models here.

class Group(TimeStampedModel):
    groupId=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=50)
    policy = models.ManyToManyField(Policy, through='GroupPolicy')

    def __unicode__(self):
        return self.name

class GroupPolicy(TimeStampedModel):
    groupPolicyId=models.AutoField(primary_key=True)
    groupId = models.ForeignKey(Group)
    policyId = models.ForeignKey(Policy)
    principalGroup=models.BooleanField(default=False)
    class Meta:
        unique_together = ("groupId", "policyId")