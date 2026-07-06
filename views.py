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
