from django.contrib import admin
from alx_travel_app.listings.models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'host')
    search_fields = ('title', 'location')
    list_filter = ('location', 'host')
# Register your models here.
