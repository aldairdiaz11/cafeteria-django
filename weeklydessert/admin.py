from django.contrib import admin
from .models import Week, Choice

# super-user credentials (aldairdiaz, codec@demy123)
# new user for step 8: (username="LeoMessi,email="leo@adiazinc.com,password=leoMessi567)
# Register your models here.

admin.site.register(Week)
admin.site.register(Choice)
