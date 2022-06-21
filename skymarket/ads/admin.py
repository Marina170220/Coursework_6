from django.contrib import admin

from ads.models import Ad, Comment

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at', 'author' )
    list_display_links = ('title', )
    list_filter = ('author', )
    ordering = ('price', 'created_at')
    search_fields = ['title']
    search_help_text = "Поиск по названию объявления"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at')
    list_display_links = ('text', )
    list_filter = ('ad', 'author', 'created_at')
    ordering = ('author', )
    search_fields = ['ad__title']
    search_help_text = "Поиск по названию объявления"
