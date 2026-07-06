from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/home.html', {'medicines': medicines})
