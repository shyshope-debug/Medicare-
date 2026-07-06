from django.shortcuts import render
from pharmacy.models import Order

def home(request):
    return render(request, 'pharmacy/home.html')

def track_order(request):
    context = {}
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        phone = request.POST.get('phone')
        try:
            order = Order.objects.get(id=order_id, customer_phone=phone)
            context['order'] = order
        except Order.DoesNotExist:
            context['error'] = 'Order not found. Check your Order ID and phone number.'
    return render(request, 'pharmacy/track_order.html', context)
