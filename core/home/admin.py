from django.contrib import admin
from .models import Address, Person

# Register your models here.
admin.site.register(Address)
admin.site.register(Person)