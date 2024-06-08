from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html




# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    #funçao paar adicionar a foto
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;" />'.format(object.photo.url))
    #nao entendi bem o que ele faz
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'create_date')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'designation')





admin.site.register(Team, TeamAdmin)
