from django.contrib import admin
from pages.models import WhatWeDo, Moderator, About

# Register your models here.


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'occupation', 'is_staff', 'created')
    list_display_links = ('name',)
    list_filter = ('name', 'school', 'location', 'is_staff')
    list_editable = ('is_staff',)
    search_fields = ('name', 'school', 'occupation', 'location', 'is_staff')
    list_per_page = 20


admin.site.register(WhatWeDo)
admin.site.register(About)
admin.site.register(Moderator, ModeratorAdmin)
