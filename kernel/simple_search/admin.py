from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "rate")
    fields = (
        ("title", "rate"),
        ("body",)
    )
    