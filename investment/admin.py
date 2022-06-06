from django.contrib import admin
from .models import Investment


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('initial_amount', 'percentage',
                    'start_date', 'end_date', 'completed')
    list_filter = ('completed',)
    search_fields = ('initial_amount', 'percentage')
    ordering = ('initial_amount',)


admin.site.register(Investment, InvestmentAdmin)
