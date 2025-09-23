from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('created_date',)
    list_editable = ('is_published',)
    list_per_page = 20


# Register your models here.
admin.site.register(Movie, MovieAdmin)