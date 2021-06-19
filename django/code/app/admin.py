from django.contrib import admin
from django.contrib.auth import User

# from django.contrib.auth.models import User
from .models import (
    ProgramingLanguage,
    Framework,
    Database,
    OperatingSystem,
    Service,
    Tool,
    Profile,
    EnglishProfile,
)


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


class EnglishProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "nickname",
        "summary",
        "introduction",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class ProgramingLanguageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class FrameworkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class DatabaseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


class ToolAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "like",
        "skilled",
        "experience_period",
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(ProgramingLanguage, ProgramingLanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Database, DatabaseAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EnglishProfile, EnglishProfileAdmin)
