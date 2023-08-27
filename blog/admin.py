from django.contrib import admin
from .models import *


# Register your models here.
class DeneyimAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1', 'title2', 'date']

    class Meta:
        model = Deneyim


admin.site.register(Deneyim, DeneyimAdmin)


class OkulAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1', 'title2', 'date']

    class Meta:
        model =Okul


admin.site.register(Okul, OkulAdmin)
