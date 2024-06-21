from django.contrib import admin
from .models import Blog, UserComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)


class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('message',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(UserComment, UserCommentAdmin)

admin.site.site_header = 'HZF Admin'
admin.site.site_title = 'HZF'
admin.site.index_title = 'Welcome'
