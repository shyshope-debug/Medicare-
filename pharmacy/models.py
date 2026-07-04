from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Clinic Admin'),
        ('DOCTOR', 'Doctor'),
        ('PHARMACIST', 'Pharmacist'),
        ('NURSE', 'Nurse'),
        ('RECEPTIONIST', 'Receptionist'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='RECEPTIONIST')
    phone = models.CharField(max_length=15, blank=True)
    license_number = models.CharField(max_length=50, blank=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')])
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Drug(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    reorder_level = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'DOCTOR'})
    diagnosis = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Prescription(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    drug = models.ForeignKey(Drug, on_delete=models.PROTECT)
    dosage = models.CharField(max_length=100)
    duration_days = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

class Sale(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    pharmacist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'PHARMACIST'})
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sold_at = models.DateTimeField(auto_now_add=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True, blank=True)
