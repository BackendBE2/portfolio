from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email',
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Subject',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Message',
        })
