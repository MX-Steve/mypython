from django.contrib import admin
from .models import Host, HostGroup , Module , Argument

# Register your models here.

for item in [HostGroup, Host, Module, Argument]:
    admin.site.register(item)