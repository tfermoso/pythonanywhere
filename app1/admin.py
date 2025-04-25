from django.contrib import admin

# Register your models here.

from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha',)
