from django.shortcuts import render
from contact.models import Contact
from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms
from . import models

class ContactForm(forms.ModelForm):

  first_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'Primeiro nome',
      }
    ),
    label='Primeiro Nome',
    help_text='Primeiro nome do contato', 
  )

  last_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'Sobrenome',
      }
    ),
    label='Sobrenome',
    help_text='Sobrenome do contato', 
  )

  phone = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'Telefone',
      }
    ),
    label='Telefone',
    help_text='Telefone do contato', 
  )

  email = forms.EmailField(
    widget=forms.TextInput(
      attrs={
        'class': 'classe-a classe-b',
        'placeholder': 'E-mail',
      }
    ),
    label='E-mail',
    help_text='E-mail do contato', 
  )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    #self.fields['first_name'].widget.attrs.update({
    #  'class': 'classe-a classe-b',
    #  'placeholder': 'Primeiro nome',
    #})

  class Meta:
    model = models.Contact
    fields = (
      'first_name', 'last_name', 'phone', 'email', 'description', 'category',
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
  

def create(request):

  if request.method == 'POST':
      context = {
         'form': ContactForm(data=request.POST or None),
      }
  
      return render(
           request, 'contact/create.html',
           context,
      )

  context = {
      'form': ContactForm()
  }

  return render(
      request, 'contact/create.html',
      context,
  )