from django.shortcuts import render

from match.forms import AddMatchForm
from match.models import Points
# Create your views here.

def add_match(request):
    form = AddMatchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            team1_score = form.cleaned_data["team_1_score"]
            team2_score = form.cleaned_data["team_2_score"]
            obj = form.save()

            if team1_score > team2_score:
                obj.winner = obj.team_1
            else:
                obj.winner = obj.team_2
            obj.save()

            score = Points()
            score.match = obj
            score.team1 = team1_score
            score.team2 = team2_score
            score.save()

            messages.add_message(request, messages.SUCCESS, "We have sent you an email, please confirm your email address to complete registration!.")
            return redirect("login")
    else:
        form = AddMatchForm()
    return render(request, 'match/add.html', {'form': form})



