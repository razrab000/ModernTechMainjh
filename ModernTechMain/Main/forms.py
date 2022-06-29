from .models import Messages
from django.forms import ModelForm, TextInput, Textarea

class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['message', 'contact']
        widgets = {
            "message": Textarea(attrs={
                'class': "your_message",
                'placeholder': 'Ваше сообщение...'
            }),
            "contact": TextInput(attrs={
                'class': 'contact_from_message',
                'placeholder': 'Контактные данные'
            })
        }