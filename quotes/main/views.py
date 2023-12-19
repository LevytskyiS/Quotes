from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from .models import Author, Quote
from .forms import AuthorForm, QuoteForm


class QuoteListView(ListView):
    model = Quote
    paginate_by = 3
    context_object_name = "quotes"
    template_name = "main/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "main/add_author.html"
    success_url = "/"


class CreateQuote(CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = "main/add_quote.html"
    success_url = "/"
