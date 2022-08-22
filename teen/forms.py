from django import forms


class PassTestForm(forms.Form):
    answer = forms.CharField(label='Ответ: ')
