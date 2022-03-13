from django.contrib import admin
from .models import Holiday
# Register your models here.

class HolidayAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')
  ordering = ('date',)

admin.site.register(Holiday, HolidayAdmin)
