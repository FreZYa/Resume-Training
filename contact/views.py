from contact.models import Message
from django.shortcuts import render
from django.http import JsonResponse

from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})

def contact_form(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Message.objects.create(name=name, email=email, subject=subject, message=message)
            contact_form.send_mail()
            return JsonResponse({'success': True,'message': 'Contact form submitted successfully'})
        else:
            return JsonResponse({'success': False,'message': 'Contact form submitted failed'})
    else:
        return JsonResponse({'success': False,'message': 'Contact form submitted failed'})