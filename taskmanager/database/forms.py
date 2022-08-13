from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "city","county","street_name","street_number","building_info","floor","apartment_number", "zip_code", "phone", "web", "email_address")
        labels = {
            "name": '',
            "city": '',
            "county": '',
            "street_name": '',
            "street_number": '',
            "building_info": '',
            "floor": '',
            "apartment_number": '',
            "zip_code": '',
            "phone": '',
            "web": '',
            "email_address": '',
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Contact Name"}),
            "city": forms.TextInput(attrs={"class": "form-control", "placeholder": "City Name"}),
            "county": forms.TextInput(attrs={"class": "form-control", "placeholder": "County Name"}),
            "street_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Street Name"}),
            "street_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Street Number"}),
            "floor": forms.TextInput(attrs={"class": "form-control", "placeholder": "Floor Number "}),
            "building_info": forms.TextInput(attrs={"class": "form-control", "placeholder": "Building info"}),
            "apartment_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apartment Number"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": " Zip Code"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "web": forms.URLInput(attrs={"class": "form-control", "placeholder": "WEB URL"}),
            "email_address": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
        }




