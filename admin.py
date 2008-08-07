from dpaste.models import Snippet
from django.contrib import admin

class SnippetAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'author',
        'lexer',
        'published',
    )

admin.site.register(Snippet, SnippetAdmin)
