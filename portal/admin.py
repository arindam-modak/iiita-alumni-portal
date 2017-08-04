from django.contrib import admin

from .models import User, Address, Qualification, WorkExperience

# Register your models here.

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Qualification)
admin.site.register(WorkExperience)
