from django.contrib import admin
from .models import Domain, DomainFlag

# Register your models here.
admin.site.register(Domain)
admin.site.register(DomainFlag)

