from django.contrib import admin

from users.models import User

admin.site.empty_value_display = '(None)'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff')
    list_display_links = ('first_name',)
    list_filter = ('is_active',)
    ordering = ('first_name',)
    empty_value_display = 'unknown'
    radio_fields = {"role": admin.VERTICAL}
    search_fields = ['email']
    search_help_text = "Поиск пользователя по email"
