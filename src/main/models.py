from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class NotaryProfile(models.Model):
    class Meta:
        db_table = "notary_profiles"

    notary = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/notary")
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    description = RichTextField(blank=True, max_length=2000)

    def __str__(self):
        return f"{self.name} {self.surname}"


class NotaryService(models.Model):
    class Meta:
        db_table = "notary_services"

    notary = models.ForeignKey(NotaryProfile, on_delete=models.CASCADE, blank=True)
    service_title = models.CharField(max_length=100, blank=True)
    service_description = RichTextField(blank=True, max_length=2000)
    service_img = models.CharField(max_length=100, blank=False)
    service_link = models.CharField(max_length=100, blank=True, null=True)
    order_num = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service_title}"


class NotaryContact(models.Model):
    class Meta:
        db_table = "notary_contacts"

    notary = models.ForeignKey(NotaryProfile, on_delete=models.CASCADE, blank=True)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    viber = models.CharField(blank=True, max_length=50)
    mapurl = models.URLField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notary} contact information"


class ContactMe(models.Model):
    class Meta:
        db_table = "contact_me"
        ordering = ["timestamp"]
        verbose_name = "Contact Me"
        verbose_name_plural = "Contact Me"

    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    name = models.CharField(max_length=50, blank=False, verbose_name="Name")
    email = models.EmailField(verbose_name="Email", blank=False, null=False)
    message = models.TextField(verbose_name="Message", max_length=1000, blank=False, null=False)
