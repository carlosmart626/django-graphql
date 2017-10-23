from django.db import models

from movies.models import Movie


class AbstractCharacter(models.Model):
    name = models.CharField(max_length=140)
    appears_in = models.ManyToManyField(Movie)

    class Meta:
        abstract = True


class HumanCharacter(AbstractCharacter):
    home_planet = models.CharField(max_length=140)
    friends = models.ManyToManyField('HumanCharacter', blank=True, null=True)

    def __str__(self):
        return self.name


class DroidCharacter(AbstractCharacter):
    primary_function = models.CharField(max_length=140)

    def __str__(self):
        return self.name
