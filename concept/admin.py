from django.contrib import admin
from .models import Concept


class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Concept, ConceptAdmin)
