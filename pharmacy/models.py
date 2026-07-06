from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # This fixes the groups/permissions clash
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="pharmacy_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="pharmacy_user_set",
        related_query_name="user",
    )

    # Patient/Pharmacy specific fields
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_patient = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)  # ADD THIS LINE
    manufacturer = models.CharField(max_length=200, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    prescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
