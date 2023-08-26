from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Post, Commentary


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("owner", "created_time",)
    ordering = ("-created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("user", "post",)
    ordering = ("-crated_time",)


admin.site.unregister(Group)
