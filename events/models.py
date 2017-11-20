from django.db import models
from django.forms import URLField
from polymorphic.models import PolymorphicModel


class Event(PolymorphicModel):
    wss = models.ForeignKey(to='WSS.WSS', related_name='events')
    title = models.CharField(max_length=150)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    venue = models.ForeignKey(to='Venue', related_name='events', null=True, blank=True)

    def __str__(self):
        return self.title


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Seminar(Event):
    abstract = models.TextField()
    is_keynote = models.BooleanField()
    material = models.OneToOneField(to='SeminarMaterial', null=True, blank=True)


class SeminarMaterial(models.Model):
    slides = models.FileField()
    videoURL = URLField()

    def __str__(self):
        return 'Material of {}'.format(self.seminar)


class Workshop(Event):
    syllabus = models.TextField()
    sponsor = models.ForeignKey(to='WSS.Sponsor', related_name='workshops', null=True, blank=True)