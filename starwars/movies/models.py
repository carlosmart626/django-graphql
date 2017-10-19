from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=140)
    year = models.PositiveIntegerField(default=1980)

    def __str__(self):
        return self.title
