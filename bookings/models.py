from django.conf import settings
from django.db import models


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="bookings",
    )
    package = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    num_tourists = models.PositiveIntegerField(default=1)
    pickup_city = models.CharField(max_length=100)
    visit_type = models.CharField(max_length=50)
    hotel_pickup = models.BooleanField(default=False)
    extras = models.JSONField(default=list, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    total_price = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.package} ({self.created_at:%Y-%m-%d})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
