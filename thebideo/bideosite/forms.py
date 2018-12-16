from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    subject = forms.CharField(label="Subject", max_length=255)
    message = forms.CharField(widget=forms.Textarea)
