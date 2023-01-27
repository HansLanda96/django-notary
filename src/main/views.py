from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import translation
from django.views.generic import FormView, TemplateView

from .forms import ContactForm
from .models import NotaryContact, NotaryProfile, NotaryService


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = NotaryService.objects.filter(pk__in=[1, 2, 3])
        context["object_list"] = object_list
        context["contacts"] = NotaryContact.objects.filter(is_active=True)
        if translation.get_language() == "en":
            context["notary"] = (
                NotaryProfile.objects.filter(name="Oleksandra").select_related("notary").first()
            )
        else:
            context["notary"] = (
                NotaryProfile.objects.filter(name="Олександра").select_related("notary").first()
            )
        return context


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = "contact_me.html"
    success_url = reverse_lazy("main:index")
    success_message = "Thank you for your message. I will provide an answer as soon as possible!"

    def get_success_message(self, cleaned_data):
        if translation.get_language() == "uk":
            return "Дякуємо за ваше повідомлення. Я зв'яжусь з вами якомога швидше!"
        else:
            return super().get_success_message(cleaned_data)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = NotaryContact.objects.filter(is_active=True)
        context["contacts"] = contacts
        if translation.get_language() == "en":
            context["notary"] = (
                NotaryProfile.objects.filter(name="Oleksandra").select_related("notary").first()
            )
        else:
            context["notary"] = (
                NotaryProfile.objects.filter(name="Олександра").select_related("notary").first()
            )
        return context


def change_theme(request, **kwargs):
    if "is_dark_theme" in request.session:
        request.session["is_dark_theme"] = not request.session.get("is_dark_theme")
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def types_view(request):
    if translation.get_language() == "en":
        notary = NotaryProfile.objects.filter(name="Oleksandra").select_related("notary").first()
    else:
        notary = NotaryProfile.objects.filter(name="Олександра").select_related("notary").first()
    contacts = NotaryContact.objects.filter(is_active=True)
    context = {"notary": notary, "contacts": contacts}
    return render(request, "types.html", context)


def switch_language(request):
    if request.method == "POST":
        language = request.POST.get("language")
        translation.activate(language)
        settings.LANGUAGE_CODE = language
    return redirect(request.META.get("HTTP_REFERER"))
