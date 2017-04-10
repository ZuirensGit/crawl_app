from django.contrib import admin

# Register your models here.
from .models import Spider, Joblog


class SpiderAdmin(admin.ModelAdmin):
    change_list_template = 'admin/crawl_change_list.html'
    list_display = ('check_spider', 'domain', 'stype', 'pages', 'url_xpath', 'release')
    list_editable = ('url_xpath', 'release')
    list_display_links = ('domain',)
    def check_spider(self, obj):
        return u'<button class="%s" id="crawl">%s</button>' % (obj.status, obj.status)
    check_spider.allow_tags = True
    check_spider.short_description = "Spider Check"

class JoblogAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'finish_time', 'status')
    readonly_fields = ('name', 'start_time', 'finish_time', 'status')
    def has_add_permission(self, request):
        return False


admin.site.register(Spider, SpiderAdmin)
admin.site.register(Joblog, JoblogAdmin)
