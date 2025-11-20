from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('firstName', 'lastName', 'email', 'phone', 'date_join', 'last_login')
    list_display_links = ('email', 'phone')
    ordering = ['date_join']
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)