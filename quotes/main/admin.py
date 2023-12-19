from django.contrib import admin

# Register your models here.
from .models import Quote, Author

admin.site.register(Quote)
admin.site.register(Author)
