from django.contrib import admin
from performer.models import PerformerModel
# Register your models here.
@admin.register(PerformerModel)
class PerformerModelAdmin(admin.ModelAdmin):
    """Админка для работы с исполнителем"""
    list_display = ('name', 'surname', 'phone', 'email', 'experience')
    search_fields = ('email',)
    ordering = ('name',)