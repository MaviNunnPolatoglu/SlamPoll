from django import forms
from .models import *
from django.contrib.auth.hashers import make_password

class CreateForm(forms.ModelForm):

    password1 = forms.CharField(required=True, widget=forms.PasswordInput, max_length=30)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput, max_length=30)

    class Meta:
        model = Poll
        exclude = ['password', 'poll_jsonstring']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'transform-lowercase'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            self.add_error('password2', 'Password did not match')

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)
        instance.password = make_password(self.cleaned_data['password1'])
        if commit:
            instance.save()
        return instance