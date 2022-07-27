from django.contrib import admin
from contacts.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created')
    list_display_links = ('name', 'email')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'created')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
