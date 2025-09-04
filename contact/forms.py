from django import forms
from .models import Message
from django.core.mail import EmailMessage
from django.conf import settings

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=254, required=True, 
        help_text='Enter your name',
    )
    email = forms.EmailField(
        max_length=254, required=True, 
        help_text='Enter your email',
    )
    subject = forms.CharField(
        max_length=254, required=True, 
        help_text='Enter your subject',
    )
    message = forms.CharField(
        max_length=254, required=True, 
        help_text='Enter your message',
    )

    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']
            message_context = 'Message received. \n\n' \
                              'Name: {name} \n' \
                              'Email: {email} \n' \
                              'Subject: {subject} \n' \
                              'Message: {message}'
            message_context = message_context.format(name=name, email=email, subject=subject, message=message)
            email = EmailMessage(subject, message_context, to=[settings.DEFAULT_FROM_EMAIL], reply_to=[email]).send()
            email.send()
            return True
        else:
            return False