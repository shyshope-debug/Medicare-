from django.contrib import admin
from .models import User, Medicine,

admin.site.register(User)
admin.site.register(Medicine)
admin.site.register(Prescription)
