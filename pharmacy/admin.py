from django.contrib import admin
from .models import User, Medicine, Order

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Order)
