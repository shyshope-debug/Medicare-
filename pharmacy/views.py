from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/home.html', {'medicines': medicines})

def order_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    
    # Example: reduce stock by 1 when ordered
    if medicine.quantity > 0:
        medicine.quantity -= 1
        medicine.save()
        
        # LOW STOCK ALERT - triggers when below 10
        if medicine.quantity < 10:
            subject = f'LOW STOCK ALERT: {medicine.name}'
            message = f'''
Medicare System Alert

Medicine: {medicine.name}
Remaining Stock: {medicine.quantity}
Threshold: 10

Action Required: Restock immediately to avoid stockout.

Sent automatically from Termux Django.
'''
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
    
    return redirect('home')
