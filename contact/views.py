from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def contact(request):
    return render(request, 'contact.html')

def contact_form(request):
    return JsonResponse({'success': True,'message': 'Contact form submitted successfully'})