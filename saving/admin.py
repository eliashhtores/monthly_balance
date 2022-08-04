from django.contrib import admin
from .models import Saving, SavingDetail


class SavingAdmin(admin.ModelAdmin):
    list_display = ('id', 'active')
    list_filter = ('active',)


class SavingDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date', 'paid', 'payback', 'received')
    list_filter = ('paid', 'received')
    search_fields = ('number',)


admin.site.register(Saving, SavingAdmin)
admin.site.register(SavingDetail, SavingDetailAdmin)
