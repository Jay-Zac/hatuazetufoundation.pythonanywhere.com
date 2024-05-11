from django.contrib import admin
from .models import Logo, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Logo)
admin.site.register(Blog, BlogAdmin)

admin.site.site_header = 'hatuazetufoundation'
admin.site.site_title = 'hatuazetu'
admin.site.index_title = 'Welcome HZF'