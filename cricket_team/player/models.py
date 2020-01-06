from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from shared.models import BaseTimestampModel
from team.models import Team


class Player(BaseTimestampModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    jersey_no = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        upload_to="player/images/", null=True, blank=True)
    country = models.CharField(max_length=50)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=40, null=True, blank=True)

    def __str__(self):
        return str(self.first_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Player, self).save(*args, **kwargs)


class PlayerHistory(BaseTimestampModel):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    matches = models.IntegerField(null=True, blank=True)
    run = models.IntegerField(null=True, blank=True)
    highest_scores = models.IntegerField(null=True, blank=True)
    fifties = models.IntegerField(null=True, blank=True)
    hundreds = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.player.first_name)
