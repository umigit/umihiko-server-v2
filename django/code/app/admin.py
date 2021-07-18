from django.contrib import admin
from .models import Profile, Skill


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


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
