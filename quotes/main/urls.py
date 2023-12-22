from django.urls import path

from . import views

# Чтобы избежать путаницы с ссылками, то перед ними можно ставить название приложение
# main:index
app_name = "main"
urlpatterns = [
    path("", views.QuoteListView.as_view(), name="index"),
    path(
        "author/<int:author_id>/",
        # "author/<slug:first_name>/",
        views.AuthorDetailView.as_view(),
        name="author_detail",
    ),
    path(
        "quote/<slug:slug>/",
        # "author/<slug:first_name>/",
        views.QuoteDetailView.as_view(),
        name="quote_detail",
    ),
    path("quote_favourite/", views.QuoteFavourite.as_view(), name="quote_favourite"),
    path("vote_up/", views.VoteUp.as_view(), name="vote_up"),
    path("add_author/", views.CreateAuthor.as_view(), name="add_author"),
    path("add_quote/", views.CreateQuote.as_view(), name="add_quote"),
]

# AuthorDetailView
# <a href="{% url 'author_detail' quote.author.first_name %}">{{ quote.author }}</a>
# for "author/<slug:first_name>/"
