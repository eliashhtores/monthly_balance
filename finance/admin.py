from django.contrib import admin
from .models import Finance


class FinanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'concept',
                    'date', 'due_date', 'paid', 'pay_date',
                    'time_frame',
                    )
    list_filter = ('paid',)
    search_fields = ('name', 'amount', 'concept')


admin.site.register(Finance, FinanceAdmin)
