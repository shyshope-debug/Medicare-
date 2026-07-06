from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

# Your existing views go here
def home(request):
    # example of your existing code from screenshot
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
    
    return redirect('home')

# ADD THIS AT THE BOTTOM - WhatsApp Webhook
VERIFY_TOKEN = "medicare_bot_verify_2026"

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        return HttpResponse('Forbidden', status=403)
    
    if request.method == 'POST':
        print("WhatsApp message received:", request.body)
        return HttpResponse('OK', status=200)
