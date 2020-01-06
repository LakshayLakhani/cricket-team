from django.db import models

from shared.models import BaseTimestampModel
from team.models import Team

class Match(BaseTimestampModel):
    team_1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="team1")
    team_2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="team2")
    winner = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="winner")

    def __str__(self):
        return str(self.winner.name)


class Points(BaseTimestampModel):
	points = models.IntegerField()
	team = models.OneToOneField(
        Team, on_delete=models.CASCADE, null=True, blank=True)
