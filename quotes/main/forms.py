from django.forms import (
    ModelForm,
    TextInput,
    Textarea,
    EmailInput,
    URLInput,
    ModelChoiceField,
)

from .models import Quote, Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "last_name": TextInput(
                attrs={"class": "form-control", "placeholder": "Surname"}
            ),
        }


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author", "slug"]
        author = ModelChoiceField(queryset=Author.objects.all())
        widgets = {
            "text": TextInput(attrs={"class": "form-control", "placeholder": "Quote"}),
            author: TextInput(attrs={"class": "form-control", "placeholder": "Author"}),
            "slug": TextInput(attrs={"class": "form-control", "placeholder": "Slug"}),
        }
