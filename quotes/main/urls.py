from django.urls import path

from . import views

urlpatterns = [
    path("", views.QuoteListView.as_view(), name="index"),
    path("add_author/", views.CreateAuthor.as_view(), name="add_author"),
    path("add_quote/", views.CreateQuote.as_view(), name="add_quote"),
]
