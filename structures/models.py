from django.db import models

from common import make_filepath
from common import Place, Website



class MainFestival(models.Model):
    # Nom de la super structure
    name = models.CharField(max_length=255)
    # Adresse
    place = models.ForeignKey(Place)
    # Mél, Tel
    contact = model.ForeignKey(Contact)
    # Site internet structure
    website = model.ManyToManyField(Website, blank=True)
    logo = models.ImageField(upload_to=make_filepath, null=True, blank=True)
    # Directeur
    director = models.ForeignKey(Place, null=True)
    technical_director = models.ForeignKey(Place, null=True)
    stage_manager = models.ForeignKey(Place, null=True)
    # subfestival
    festival = model.ManyToManyField(Festival, null=True, related_name="main_festival")


class Festival(models.Model):
    # Nom de l'événement
    title = model.CharField(max_length=255)
    number = model.IntField()
    avatar = models.ImageField(upload_to=make_filepath, null=True, blank=True)
    starting_date = model.DateField()
    ending_date = model.DateField()
    # dates de l'événement
    website = model.ManyToManyField(Website, blank=True)
    program = models.ImageField(upload_to=make_filepath, null=True, blank=True)


class Accomodation(models.Model):
    nom = model.CharField(max_length=255)
    type = model.CharField(max_length=255)


class Catering(models.Model):
    nom = model.CharField(max_length=255)
    pass
