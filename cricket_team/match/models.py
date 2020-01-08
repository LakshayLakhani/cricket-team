from django.db import models

from shared.models import BaseTimestampModel
from team.models import Team

class Points(BaseTimestampModel):
    # match = models.OneToOneField(Match, on_delete=models.CASCADE, null=True, blank=True)
    team1 = models.IntegerField(null=True, blank=True)
    team2 = models.IntegerField(null=True, blank=True)


class Match(BaseTimestampModel):
    team_1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="team1")
    team_2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="team2")
    winner = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True, related_name="winner")
    score = models.OneToOneField(Points, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} vs {}'.format(self.team_1, self.team_2)




# class Points(BaseTimestampModel):
#     team1 = models.IntegerField()
#     team2 = models.IntegerField()
#     team = models.ForeignKey(
#         Team, on_delete=models.CASCADE, null=True, blank=True)
#     match = models.ForeignKey(
#         Match, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return str(self.team)

# class Score():


