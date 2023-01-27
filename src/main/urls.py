from django.urls import path

from .views import ContactView, IndexView, change_theme, switch_language, types_view

app_name = "main"

urlpatterns = [
    path("switch-theme/", change_theme, name="change-theme"),
    path("set-language/", switch_language, name="set-lang"),
    path("", IndexView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("types/", types_view, name="types"),
]
