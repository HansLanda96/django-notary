from modeltranslation.translator import TranslationOptions, register

from .models import NotaryProfile, NotaryService


@register(NotaryProfile)
class NotaryProfileTranslationOptions(TranslationOptions):
    fields = ("name", "surname", "description")


@register(NotaryService)
class NotaryServiceTranslationOptions(TranslationOptions):
    fields = ("service_title", "service_description")
