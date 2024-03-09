from django.contrib import admin

# Register your models here.
from pinkslips.models import PinkSlip, Appointments, InventoryItem, Billing

class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'expiration_date')
    list_filter = ('inventory_type', 'expiration_date')
    search_fields = ('item_name', 'supplier_information')
    ordering = ('item_name',)
    date_hierarchy = 'expiration_date'

class BillingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'insurance_details', 'total_amount', 'paid', 'payment_date', 'transaction_id')
    list_filter = ('paid', 'payment_date')
    search_fields = ('patient__firstname', 'patient__lastname', 'insurance_details', 'transaction_id')
    ordering = ('-payment_date',)


admin.site.register(PinkSlip)
admin.site.register(Appointments)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(Billing, BillingAdmin)
