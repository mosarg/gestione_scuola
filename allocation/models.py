from django.db import models
from django_extensions.db.models import TimeStampedModel
from school.models import Class, School, Subject
from sysuser.models import SysUser



class Role(TimeStampedModel):
    roleId=models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    ou=models.CharField(max_length=45,default='default');

    def __unicode__(self):
        return self.name


class SchoolYear(TimeStampedModel):
    schoolYearId=models.AutoField(primary_key=True)
    year = models.PositiveIntegerField(unique=True)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.year)


class Allocation(TimeStampedModel):
    allocationId=models.AutoField(primary_key=True)
    yearId = models.ForeignKey(SchoolYear)
    userId = models.ForeignKey(SysUser, related_name='allocation')
    roleId = models.ForeignKey(Role)
    ou = models.CharField(max_length=50, default='default')
    
    class Meta:
        unique_together = ("yearId", "userId")

    def __unicode__(self):
        return '('+unicode(self.yearId)+','+unicode(self.userId)+','+unicode(self.roleId)+')'


class NonDidacticalAllocation(TimeStampedModel):
    nonDidacticalAllocationId = models.AutoField(primary_key=True)
    allocationId = models.ForeignKey(Allocation, related_name='nondidactical_allocation')
    schoolId = models.ForeignKey(School)


class DidacticalAllocation(TimeStampedModel):
    didacticalAllocationId=models.AutoField(primary_key=True)
    allocationId = models.ForeignKey(Allocation, related_name='didactical_allocation')
    classId = models.ForeignKey(Class)
    subjectId = models.ForeignKey(Subject)

    class Meta:
        unique_together = ("classId", "subjectId", "allocationId")


