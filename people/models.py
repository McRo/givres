from django.contrib.auth.models import User
from django.db import models

from common.utils import make_filepath

class Human(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, related_name='profile')

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    email = models.CharField(max_length=255, null=False, blank=False)

    photo = models.ImageField(upload_to=make_filepath, blank=True, null=True)

    birthdate = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)



class Artist(models.Model):
    human = models.ForeignKey(Human, blank=True)
    nickname = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.human, self.nickname)


class Reporter(models.Model):
    human = models.ForeignKey(Human)
    media = models.ManyToManyField('people.Organisation', blank=True, related_name='Reporters')


class Technician(models.Model):
    human = models.ForeignKey(Human)


class Organization(models.Model):
    TYPES_CHOICES = (
        ('M', 'MEDIA'),
        ('L', 'LABEL'),
        ('F', 'FESTIVAL'),
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=TYPES_CHOICES, null=True, blank=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to=make_filepath, blank=True)

    def __unicode__(self):
        return self.name
