from django.contrib import admin
from .models import Saving


class SavingAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date', 'paid', 'payback')
    list_filter = ('paid',)
    search_fields = ('number',)


admin.site.register(Saving, SavingAdmin)
