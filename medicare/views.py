from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

VERIFY_TOKEN = "medicare123" # MUST match what you put in Meta
WHATSAPP_TOKEN = "EAATkdgwiB4wBRwBZCA4tDBZCdUPog8CB82wdB2KSZBXnXZCPMpNFex6FbyrMGJiwpefeDJRGfMD0ZCTNe1O5i2vzbRnKMf4eJ9YSOCgzkj5d07XXw7LKFO4wGxZAlYUE9ZB0A7ZAZAvtzxaZBserw946ZBHvDBew0XhpVQO6JqY7x9szSLEKRyZBU73LGbDvdvwEfZCBnOg5WQZCpxDKYKLvd7eeKkEvAh2dKGZBLh0Q2MxTa3quRzi8lnnbfOSHcVeBi18gSx0nkma9UDJ3ZAjWCH1g9RewF7qCKE0uyqoGZBrMrGgZDZD"
PHONE_NUMBER_ID = "1205280212666945"

@csrf_exempt
def webhook(request):
    # 1. Meta verification
    if request.method == 'GET':
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('Forbidden', status=403)

    # 2. Handle incoming messages
    elif request.method == 'POST':
        data = json.loads(request.body)
        print("[Webhook] Received:", data)
        
        if 'entry' in data:
            for entry in data['entry']:
                for change in entry['changes']:
                    if 'messages' in change['value']:
                        message = change['value']['messages'][0]
                        from_number = message['from']
                        text = message['text']['body']
                        
                        # Reply back to user
                        reply_text = f"You said: {text}"
                        send_message(from_number, reply_text)
        
        return HttpResponse('ok', status=200)

def send_message(to, text):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=data)
