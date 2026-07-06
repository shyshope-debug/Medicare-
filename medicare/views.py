from django.shortcuts import render
from django.http import HttpResponse

def track_order(request):
    status = None
    phone = ""
    
    if request.method == 'POST':
        phone = request.POST.get('phone', '')
        # For now just show a dummy status
        # Replace this with real Order lookup later
        if phone:
            status = "Order Received - Preparing"
        else:
            status = "No order found for this number"
    
    return render(request, 'track.html', {'status': status, 'phone': phone})
