from django.contrib import admin

# Register your models here.
from .models import Spider, Joblog


class SpiderAdmin(admin.ModelAdmin):
    list_display = ('domain', 'pages', 'url_xpath', 'title_xpath', 'content_xpath', 'author_xpath', 'date_xpath', 'status')
    list_editable = ('url_xpath', 'title_xpath', 'content_xpath', 'author_xpath', 'date_xpath')


class JoblogAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'finish_time', 'status')
    readonly_fields = ('name', 'start_time', 'finish_time', 'status')
    def has_add_permission(self, request):
        return False


admin.site.register(Spider, SpiderAdmin)
admin.site.register(Joblog, JoblogAdmin)
