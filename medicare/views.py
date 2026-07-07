from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

VERIFY_TOKEN = "medicare123" # MUST match Meta

@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        # Meta verification
        mode = request.GET.get('hub.mode')
        token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')
        
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('Forbidden', status=403)
    
    elif request.method == 'POST':
        # Handle incoming messages
        data = json.loads(request.body)
        print("[Webhook] Received:", data)
        return HttpResponse('ok', status=200)
