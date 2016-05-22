from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder': 'Your email address (optional)'}))

    class Meta:
        model = Message
        fields = ('content', 'email',)