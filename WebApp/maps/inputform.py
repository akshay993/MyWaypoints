from django import forms


class InputForm(forms.Form):
    Start = forms.CharField(label='Start Location', max_length=100)
    End = forms.CharField(label='Destination', max_length=100)