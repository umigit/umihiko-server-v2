from django.db import (
    models,
)
from django.contrib.auth.models import (
    User,
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    locale = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=200, null=False, default="")
    summary = models.TextField(
        blank=True,
        default="",
    )
    introduction = models.TextField(
        blank=True,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProgramingLanguage(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Framework(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Database(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OperatingSystem(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tool(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
    )
    experience_period = models.CharField(
        max_length=200,
        blank=True,
        default="",
    )
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
