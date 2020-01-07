from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from team.models import Team
from player.models import Player


class TeamListView(ListView):
    model = Team
    queryset = Team.objects.all()
    # template_name = "team/list.html"


class TeamDetailView(DetailView):
	model = Team

	def get_context_data(self, *args, **kwargs):
		context = super(TeamDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		players = Player.objects.filter(team=obj)
		context["players"] = players
		return context



