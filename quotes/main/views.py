import json
import time

from django.http import JsonResponse
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Quote
from .forms import AuthorForm, QuoteForm


class QuoteListView(ListView):
    model = Quote
    paginate_by = 3
    context_object_name = "quotes"
    template_name = "main/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()


class AuthorDetailView(DetailView):
    model = Author
    # По умолчанию Django ищет шаблон в каталоге <application_name>/<model_name>_detail.html, т.е. blog/post_detail.html
    template_name = "main/author_detail.html"
    # AttributeError is raised if pk is None and slug is None
    pk_url_kwarg = "author_id"
    # OR
    # slug_url_kwarg = "first_name"
    # slug_field = "first_name"


class QuoteDetailView(DetailView):
    model = Quote
    template_name = "main/quote_detail.html"
    # pk_url_kwarg = "quote_id"


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


class VoteUp(APIView):
    def post(self, request):
        data = json.loads(request.body)
        vote = int(data.get("value"))
        quote_id = int(data.get("quoteId"))
        # quote = Quote.objects.get(id=quote_id)
        quote = get_object_or_404(Quote, pk=quote_id)
        quote.rating += 1
        quote.save()
        return Response(json.dumps({"voted": "Voted"}))


# function
# def vote_up(request):
#     data = json.loads(request.body)
#     vote = int(data.get("value"))
#     quote_id = int(data.get("quoteId"))
#     # quote = Quote.objects.get(id=quote_id)
#     quote = get_object_or_404(Quote, pk=quote_id)
#     quote.rating += 1
#     quote.save()
#     print(quote.rating)
#     return JsonResponse("Voted!", safe=False)
