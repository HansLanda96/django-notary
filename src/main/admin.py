from django.contrib import admin

from .models import ContactMe, NotaryContact, NotaryProfile, NotaryService


@admin.register(NotaryProfile)
class NotaryProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")


@admin.register(NotaryService)
class NotaryServiceAdmin(admin.ModelAdmin):
    list_display = ("service_title", "order_num", "is_active")


@admin.register(NotaryContact)
class NotaryContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "is_active")


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "timestamp")
