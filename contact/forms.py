from django.shortcuts import render
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import Contact
from django import forms
from . import models

class ContactForm(forms.ModelForm):

  picture = forms.ImageField(
    widget=forms.FileInput(
      attrs={
        'accept': 'image/*',
      }
    )
  )

  class Meta:

    model = models.Contact
    fields = (
      'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
    )

  def clean(self):
    
    cleaned_data = self.cleaned_data
    first_name = cleaned_data.get('first_name')
    last_name = cleaned_data.get('last_name')

    if first_name == last_name:
      self.add_error('last_name',  ValidationError('Primeiro nome e sobrenome devem ser diferentes', code='invalid'))

    return super().clean()

  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')
    if first_name is not None and len(first_name) < 3:
      self.add_error('first_name',  ValidationError('Primeiro nome inválido, tamanho inválido', code='invalid'))
    return first_name
  
class RegisterForm(UserCreationForm):
  first_name = forms.CharField(required=True, min_length=3)
  last_name = forms.CharField(required=True, min_length=3)
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

  def clear_email(self):
    email = self.cleaned_data.get('email')

    if(User.objects.filter(email=email).exists()):
      self.add_error('email',  ValidationError('Email ja existe', code='invalid'))

    return email

class RegisterUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')