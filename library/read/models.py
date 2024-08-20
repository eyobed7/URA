from django.db import models
from django.contrib.auth.models import AbstractUser

class User1(AbstractUser):
    ROLE = [
        ('Admin', 'Admin'),
        ('MEMBER', 'MEMBER'),
        ('LIBRARY', 'LIBRARY'),
    ]
    role = models.CharField(max_length=24, choices=ROLE, default='MEMBER')

    def __str__(self):
        return f"{self.username} ({self.role})"

    

