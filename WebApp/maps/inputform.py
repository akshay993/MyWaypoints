from django import forms
from maps.models import DataTable

#class InputForm(forms.Form):
#
#    MODE_CHOICES = [ ('DRIVING', 'DRIVING'), ('WALKING', 'WALKING'), ('TRANSIT', 'TRANSIT') ]
#
#    Start = forms.CharField(label='Start Location', max_length=100)
#    End = forms.CharField(label='Destination', max_length=100)
#    Mode = forms.CharField(label='Mode', widget=forms.Select(choices=MODE_CHOICES))



class InputForm(forms.ModelForm):

    MODE_CHOICES = [ ('DRIVING', 'DRIVING'), ('WALKING', 'WALKING'), ('TRANSIT', 'TRANSIT') ]

    Start = forms.CharField(label='Start Location', max_length=100)
    End = forms.CharField(label='Destination', max_length=100)
    Mode = forms.CharField(label='Mode', widget=forms.Select(choices=MODE_CHOICES))

    class Meta:
        model = DataTable
        fields = ('Start', 'End', 'Mode',)