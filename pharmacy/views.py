from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.filter(available=True)
    return render(request, 'pharmacy/home.html', {'medicines': medicines})
