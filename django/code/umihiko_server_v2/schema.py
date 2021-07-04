from django.db.models.fields import IntegerField
from graphene import Schema, ObjectType, List, Field, Int
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from app.models import Profile, Skill


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
        fields = ("nickname", "summary", "introduction")


class Query(ObjectType):
    user = Field(UserType, id=Int(required=True))

    def resolve_user(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None


schema = Schema(query=Query)
