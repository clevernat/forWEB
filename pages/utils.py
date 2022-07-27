# from contacts.models import Contact
# from django.forms import ModelForm  # widgets
from django import forms
from tinymce import TinyMCE
from pages.models import Moderator


# class ContactForm(forms.ModelForm):
#     class Meta:
#         models = Contact
#         fields = fields = ('name', 'email', 'phone', 'message')


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Moderator
        fields = '__all__'
