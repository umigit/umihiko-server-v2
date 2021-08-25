from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    locale = models.CharField(max_length=20, null=False)
    nickname = models.CharField(max_length=200, null=False, default="")
    summary = models.TextField(blank=True, default="")
    introduction = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname


class Skill(models.Model):
    class Category(models.IntegerChoices):
        LANGUAGE = 0, "Language"
        FRAMEWORK = 1, "Framework"
        DATABASE = 2, "Database"
        OPETATING_SYSTEM = 3, "Operating System"
        SERVICE = 4, "Service"
        TOOL = 5, "Tool"

    name = models.CharField(max_length=200, null=False)
    category = models.IntegerField(choices=Category.choices, null=True)
    experience_period = models.CharField(max_length=200, blank=True, default="")
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=200, null=False)
    picture = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft"
        FUTURE = "future"
        PUBLISH = "publish"
        PRIVATE = "private"
        TRASH = "trash"

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posts")
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
    )
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    slug = models.CharField(max_length=200, blank=False, unique=True)
    title = models.CharField(max_length=200, null=False, default="")
    introduction = models.TextField(max_length=400, null=False)
    markdown = MarkdownxField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        null=False,
    )
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
