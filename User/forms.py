from django import forms

from django.contrib.auth.forms import UserCreationForm
from . models import User, Profile, ProfileMoreInfo



class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email',  'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class ProfileMoreInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileMoreInfo

        fields = ['firstName', 'lastName']

