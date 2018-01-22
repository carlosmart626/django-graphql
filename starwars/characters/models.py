from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels import Group

from movies.models import Movie


class AbstractCharacter(models.Model):
    name = models.CharField(max_length=140)
    appears_in = models.ManyToManyField(Movie)

    class Meta:
        abstract = True


class HumanCharacter(AbstractCharacter):
    home_planet = models.CharField(max_length=140)
    friends = models.ManyToManyField('HumanCharacter', blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=HumanCharacter)
def send_update(sender, instance, created, *args, **kwargs):
    uuid = str(instance.uuid)
    if created:
        Group("gqp.character-add").send({'added': True})
        return
    Group('gqp.character-updated.{0}'.format(uuid))\
        .send({'text': uuid})


class DroidCharacter(AbstractCharacter):
    primary_function = models.CharField(max_length=140)

    def __str__(self):
        return self.name
