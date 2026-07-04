from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Drug, Consultation, Prescription, Sale

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Drug)
admin.site.register(Consultation)
admin.site.register(Prescription)
admin.site.register(Sale)
