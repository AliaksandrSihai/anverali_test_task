from django.contrib import admin

from customer.models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Админка для работы с заказчиком"""

    list_display = ("name", "surname", "phone", "email", "experience")
    search_fields = ("email",)
    ordering = ("name",)
