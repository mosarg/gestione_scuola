from django.db import models
from django_extensions.db.models import TimeStampedModel

class School(TimeStampedModel):
    schoolId=models.AutoField(primary_key=True)
    meccanographic = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    ou = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Class(TimeStampedModel):
    classId=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    ou = models.CharField(max_length=30)
    capacity = models.PositiveIntegerField(default=20)
    schoolId = models.ForeignKey(School)
    aggregate=models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Subject(TimeStampedModel):
    subjectId=models.AutoField(primary_key=True)
    code = models.PositiveIntegerField(unique=True)
    description = models.CharField(max_length=200)
    shortDescription = models.CharField(max_length=100)
    niceName = models.CharField(max_length=50)

    def __unicode__(self):
        return self.shortDescription

