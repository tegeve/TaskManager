from .forms import  ContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from calendar import HTMLCalendar, calendar
from datetime import datetime
from django.shortcuts import render,redirect

def home(request):
    name = 'John'
    return render(request,
                  'templates/database/home.html', {
                      'name': name,
                  })


def add_contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_contact?submitted=True")
    else:
        form = ContactForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'templates/database/add_contact.html', {"form": form, "submitted": submitted})

def list_contact(request):
    contact_list = Contact.objects.all()
    return render(request, 'templates/database/list_contact.html', {'list_contact': contact_list})

def show_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render(request, 'templates/database/show_contact.html', {'contact': contact})

def update_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('list-contact')
    return render(request, 'templates/database//update_contact.html', {'contact': contact, 'form': form})

def delete_contact(request, contact_id):
    contact= Contact.objects.get(pk=contact_id)
    contact.delete()
    return redirect('list-contact')
