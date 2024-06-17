from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from contact.models import Contact

from contact.forms import ContactForm
from contact.models import Contact

def create(request):
  if request.method == 'POST':
      
    form = ContactForm(request.POST)

    context = {
        'form': form
    }
    
    if form.is_valid():
      print('formulario é valido')
      
      #contact = form.save(commit=False)
      #contact.show = False
      #contact.save() 
      contact = form.save()
      print(contact)

      return redirect('contact:create')
      #return redirect('contact:contact', contact.id)

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
