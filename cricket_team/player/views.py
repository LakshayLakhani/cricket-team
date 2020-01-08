from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from player.models import Player
from player.forms import AddPlayerForm


class PlayerListView(ListView):
    model = Player
    queryset = Player.objects.all()
    template_name = "player/player_list.html"


class PlayerDetailView(DetailView):
	model = Player

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
	# 	obj = self.get_object()
	# 	players = Player.objects.filter(team=obj)
	# 	context["players"] = players
	# 	return context


def AddPlayer(request):
    form = AddPlayerForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            # messages.add_message(request, messages.SUCCESS, "We have sent you an email, please confirm your email address to complete registration!.")
            return redirect("add_player")
    else:
        form = AddPlayerForm()
    return render(request, 'player/add_player.html', {'form': form})


	


