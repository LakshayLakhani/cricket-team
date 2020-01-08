from django import forms

from team.models import Team


class AddTeamForm(forms.ModelForm):
    # team_1_score = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}))
    # team_2_score = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}))

    class Meta:
        model = Team
        fields = ('name', 'logo', 'club', 'state')

    def __init__(self, *args, **kwargs):
        super(AddTeamForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['logo'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['club'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['state'].widget.attrs.update({'class': 'form-control', 'required':True})

    def clean_name(self):
        cleaned_data = super(AddTeamForm, self).clean()
        name = cleaned_data.get("name")

        if Team.objects.filter(name=name).exists():
            raise forms.ValidationError("This name already exists.")


        return self.cleaned_data['name']