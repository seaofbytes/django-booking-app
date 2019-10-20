from django.contrib import admin
from booking.models import Apartment, Reservation, ApartmentImages, ApartmentPrices
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
# Register your models here.

admin.site.register(Apartment)
admin.site.register(Reservation)
admin.site.register(ApartmentImages)
admin.site.register(ApartmentPrices)

class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ApartmentImages
    fields = ['image_tag']
    readonly_fields = ['image_tag']


class ApartmentAdmin(SortableAdminMixin, admin.ModelAdmin):

    inlines = (ImagesInline,)

