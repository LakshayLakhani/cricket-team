from django import forms

from player.models import Player


class AddPlayerForm(forms.ModelForm):
    # team_1_score = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}))
    # team_2_score = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required':'required'}))

    class Meta:
        model = Player
        fields = ('first_name','last_name', 'jersey_no', 'image', 'country', 'team')

    def __init__(self, *args, **kwargs):
        super(AddPlayerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['jersey_no'].widget.attrs.update({'class': 'form-control', 'required':True})
        self.fields['team'].widget.attrs.update({'class': 'form-control', 'required':True})

    # def clean_name(self):
    #     cleaned_data = super(AddTeamForm, self).clean()
    #     name = cleaned_data.get("name")

    #     if Team.objects.filter(name=name).exists():
    #         raise forms.ValidationError("This name already exists.")


    #     return self.cleaned_data['name']