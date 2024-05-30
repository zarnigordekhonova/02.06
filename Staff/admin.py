from django.contrib import admin
from .models import Workers, Jobs, Company
# Register your models here.

admin.site.register(Workers)
admin.site.register(Jobs)
admin.site.register(Company)