from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.filter(stock_quantity__gt=0).order_by('name')
    return render(request, 'home.html', {'medicines': medicines})
