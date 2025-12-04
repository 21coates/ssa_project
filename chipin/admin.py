from django.contrib import admin
from .models import Group

@admin.register(Group) # Register the admin model
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "admin")
