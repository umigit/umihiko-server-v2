from graphene import Schema, ObjectType, List, Field, Int, String, relay
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from app.models import Profile, Skill, BlogPost, Image, BlogCategory
import os


class SkillType(DjangoObjectType):
    class Meta:
        model = Skill
        fields = ("name", "experience_period", "skilled", "like")


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "email", "profiles")

    languages = List(SkillType)
    frameworks = List(SkillType)
    databases = List(SkillType)
    operating_systems = List(SkillType)
    services = List(SkillType)
    tools = List(SkillType)

    def resolve_languages(self, info):
        try:
            return Skill.objects.filter(category=0)
        except Skill.DoesNotExist:
            return None

    def resolve_frameworks(self, info):
        try:
            return Skill.objects.filter(category=1)
        except Skill.DoesNotExist:
            return None

    def resolve_databases(self, info):
        try:
            return Skill.objects.filter(category=2)
        except Skill.DoesNotExist:
            return None

    def resolve_operating_systems(self, info):
        try:
            return Skill.objects.filter(category=3)
        except Skill.DoesNotExist:
            return None

    def resolve_tools(self, info):
        try:
            return Skill.objects.filter(category=4)
        except Skill.DoesNotExist:
            return None


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("nickname", "summary", "introduction", "locale")


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = ("title",)

    url = String()

    def resolve_url(self, info):
        return f"{os.environ['GS_BUCKET_URL']}/{self.picture}"


class BlogPostType(DjangoObjectType):
    class Meta:
        model = BlogPost
        interfaces = (relay.Node,)
        fields = (
            "slug",
            "title",
            "introduction",
            "markdown",
            "published_at",
            "updated_at",
        )

    image = Field(ImageType)
    category = String()

    def resolve_image(self, info):
        return self.image

    def resolve_category(self, info):
        return self.category.name


class BlogPostConnection(relay.Connection):
    class Meta:
        node = BlogPostType


class Query(ObjectType):
    user = Field(UserType, username=String(required=True))
    blog_posts = relay.ConnectionField(BlogPostConnection, category=String())
    blog_post_by_slug = Field(BlogPostType, slug=String(required=True))

    def resolve_user(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def resolve_blog_posts(root, info, **kwargs):
        try:
            if kwargs.get("category") is None:
                return BlogPost.objects.all().order_by("-published_at")
            else:
                return BlogPost.objects.filter(
                    category__name=kwargs.get("category")
                ).order_by("-published_at")
        except BlogPost.DoesNotExist:
            return None

    def resolve_blog_post_by_slug(root, info, slug):
        try:
            return BlogPost.objects.get(slug=slug)
        except BlogPost.DoesNotExist:
            return None


schema = Schema(query=Query)
