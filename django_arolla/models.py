from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    job = models.ForeignKey(Job, blank=True, null=True) # metier
    skills = models.ManyToManyField(Skill, blank=True, null=True) # competences

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
