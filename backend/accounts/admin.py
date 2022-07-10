from django.contrib import admin
from .models import Info
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(Info, InfoAdmin)