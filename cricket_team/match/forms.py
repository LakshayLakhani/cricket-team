from django import forms

from match.models import Match

class AddMatchForm(forms.ModelForm):
    team_1_score = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'required'}))
    team_2_score = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'required'}))

    class Meta:
        model = Match
        fields = ('team_1', 'team_2')

    def __init__(self, *args, **kwargs):
        super(AddMatchForm, self).__init__(*args, **kwargs)
        self.fields['team_1'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['team_2'].widget.attrs.update({'class': 'form-control', 'required':True})
        # self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'required':True})
        # self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'required':True})

    def clean_team_2(self):
        cleaned_data = super(AddMatchForm, self).clean()
        team_1 = cleaned_data.get("team_1")
        team_2 = cleaned_data.get("team_2")

        if team_1 == team_2:
        	raise forms.ValidationError("match between 2 same team not possible.")

        return self.cleaned_data['team_2']