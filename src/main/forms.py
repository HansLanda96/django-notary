from django import forms

from .models import ContactMe


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ("name", "email", "message")

    name = forms.CharField(
        max_length=50,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={"class": "qwa", "placeholder": "Ivan Ivanovic"})
    )

    email = forms.EmailField(
        required=True,
        max_length=254,
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "qwa", "placeholder": "ivan@ivanovic.com"}),
    )

    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea(attrs={"class": "qwa", "placeholder": "Ask your question!"}),
    )
