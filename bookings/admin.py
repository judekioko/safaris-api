from django.contrib import admin

from .models import Booking, ContactMessage


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "full_name", "package", "start_date", "end_date",
        "num_tourists", "total_price", "created_at",
    )
    list_filter = ("pickup_city", "visit_type", "hotel_pickup")
    search_fields = ("full_name", "email", "phone", "package")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
