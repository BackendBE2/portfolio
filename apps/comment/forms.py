from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = "__all__"
        exclude = ["blog"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'name...',
        })
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'image...',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'email...',
        })
        self.fields['website'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'subject...',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'message...',
        })