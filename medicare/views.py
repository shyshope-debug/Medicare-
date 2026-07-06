from django.shortcuts import render
from .models import Order  # assumes you have Order model

def track_order(request):
    status = None
    if request.method == 'POST':
        phone = request.POST.get('phone')
        try:
            order = Order.objects.filter(phone=phone).latest('created_at')
            status = order.status
        except Order.DoesNotExist:
            status = 'Not found'
    return render(request, 'track.html', {'status': status})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order  # delete this line if you don't have Order model yet

def track_order(request):
    status = None
    phone = ""
    
    if request.method == 'POST':
        phone = request.POST.get('phone', '')
        # Change this query to match your actual Order model
        try:
            order = Order.objects.filter(phone=phone).latest('created_at')
            status = order.status  # Should be 'Paid', 'Preparing', 'Delivered', etc
        except:
            status = 'No order found for this number'
    
    return render(request, 'track.html', {'status': status, 'phone': phone})
