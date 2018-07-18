from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
   email = forms.EmailField(required=True)
   class Meta:
       model = User
       fields = (
           'username',
           'first_name',
           'last_name',
           'email',
           'password1',
           'password2'
       )

   def save(self, commit=True):
       user = super(RegistrationForm, self).save(commit=False)
       user.first_name = ['first_name']
       user.last_name = ['last_name']
       user.email = ['email']



       if commit:
           user.save()


           return user