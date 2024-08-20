from django.contrib import admin
from .models import User1

@admin.register(User1)
class User1Admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  # Customize the list display as needed
    search_fields = ('username', 'email')  # Add search functionality
    list_filter = ('role',)  # Add filters by role

