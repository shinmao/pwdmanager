from allauth.account.forms import SignupForm
from django import forms

class SignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class SecretEditForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Email you use to log in to the website')
    password = forms.CharField(
            max_length=100,
            widget=forms.Textarea(),
            help_text='Input other secrets here less than 300 characters!'              )
    notes = forms.CharField(
            max_length=300,
            widget=forms.Textarea(),
            help_text='Input other secrets here less than 300 characters!'              )
    def clean(self):
        cleaned_data = super(SecretEditForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        notes = cleaned_data.get("notes")
        if not username and not email and not password and not notes:
            raise forms.ValidationError("You just changed nothing!")

class SecretForm(forms.Form):
    website = forms.CharField(max_length=100)
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Email you use to log in to the website')
    password = forms.CharField(
            max_length=100,
            widget=forms.Textarea(),
            help_text='Input your password less than 100 characters!'
            )
    notes = forms.CharField(
            max_length=300,
            widget=forms.Textarea(),
            help_text='Input other secrets here less than 300 characters!'
            )
    def clean(self):
        cleaned_data = super(SecretForm, self).clean()
        website = cleaned_data.get("website")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        notes = cleaned_data.get("notes")
        if not website and not username and not email and not password and not notes:
            raise forms.ValidationError("You have to give me some secret!")
