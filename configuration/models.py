from django.db import models
from django_extensions.db.models import TimeStampedModel
from allocation.models import Role
from account.models import Policy
from group.models import Group
from backend.models import Backend


class Profile(TimeStampedModel):
    profileId=models.AutoField(primary_key=True)
    role=models.ForeignKey(Role)
    defaultPolicy=models.ForeignKey(Policy)
    mainGroup=models.ForeignKey(Group)
    backendId=models.ForeignKey(Backend)
    name=models.CharField(max_length=100, default='profile')


    class Meta:
        unique_together= ("role","backendId")

    def __unicode__(self):
        return self.name