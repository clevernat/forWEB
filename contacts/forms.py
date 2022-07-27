from django.forms import ModelForm  # widgets
from django import forms
from contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control shadow-none py-3', 'id': 'name',
                'placeholder': 'Enter your full name..', 'name': 'name', 'autocomplete': 'off'},
        )

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control shadow-none py-3', 'id': 'email',
                'placeholder': 'Enter your email address', 'name': 'email', 'autocomplete': 'off'},
        )

        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control shadow-none py-3', 'id': 'phone',
                'placeholder': 'Enter your phone number', 'name': 'phone', 'autocomplete': 'off'},
        )

        self.fields['message'].widget.attrs.update(
            {'class': 'form-control shadow-none', 'id': 'message',
                'placeholder': 'Reasons for contacting Us...', 'name': 'message', 'autocomplete': 'off'},
        )

        # for name, field in self.fields.items():
        #     field.widget.attrs.update(
        #         {'class': 'form-control shadow-none py-3', 'autocomplete': 'off'})
