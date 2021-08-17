from django.db import models
from django.contrib import admin
from markdownx.widgets import AdminMarkdownxWidget
from .models import Profile, Skill, Image, BlogCategory, BlogPost


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nickname",
        "summary",
        "introduction",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "picture", "created_at", "updated_at")
    ordering = ("-created_at",)


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    ordering = ("-created_at",)


class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": AdminMarkdownxWidget},
    }
    list_display = (
        "title",
        "introduction",
        "status",
        "category",
        "slug",
        "published_at",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
