from django.shortcuts import render
from django.views.generic.list import ListView

from team.models import Team


class TeamListView(ListView):
    model = Team
    queryset = Team.objects.all()
    template_name = "team/list.html"
