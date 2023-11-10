from django.contrib import admin
from .models import Url, Uygulamalar

# Register your models here.
class UygulamalarAdmin(admin.ModelAdmin):
    list_display = ['ad']

admin.site.register(Uygulamalar, UygulamalarAdmin)

class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'uyg']

admin.site.register(Url, UrlAdmin)