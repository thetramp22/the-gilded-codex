from django.contrib import admin
from .models import InventoryItem, MiniatureDetails, SupplyDetails

# Register your models here.

admin.site.register(InventoryItem)
admin.site.register(MiniatureDetails)
admin.site.register(SupplyDetails)
