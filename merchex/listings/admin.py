from django.contrib import admin
from listings.models import Band, Listing

# Register your models here.
admin.site.register(Band)
admin.site.register(Listing)

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')