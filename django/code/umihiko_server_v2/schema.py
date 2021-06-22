from graphene import Schema, ObjectType, List, Field, String
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from app.models import (
    ProgramingLanguage,
    Framework,
    Database,
    OperatingSystem,
    Service,
    Tool,
    Profile,
)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("username", "email", "profiles")


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        filter_fields = ("nickname", "summary", "introduction")


class ProgramingLanguageType(DjangoObjectType):
    class Meta:
        model = ProgramingLanguage
        fields = ("name", "experience_period", "skilled", "like")


class FrameworkType(DjangoObjectType):
    class Meta:
        model = Framework
        fields = ("name", "experience_period", "skilled", "like")


class DatabaseType(DjangoObjectType):
    class Meta:
        model = Database
        fields = ("name", "experience_period", "skilled", "like")


class OperatingSystemType(DjangoObjectType):
    class Meta:
        model = OperatingSystem
        fields = ("name", "experience_period", "skilled", "like")


class ServiceType(DjangoObjectType):
    class Meta:
        model = Service
        fields = ("name", "experience_period", "skilled", "like")


class ToolType(DjangoObjectType):
    class Meta:
        model = Tool
        fields = ("name", "experience_period", "skilled", "like")


class Query(ObjectType):
    programing_languages = List(ProgramingLanguageType)
    frameworks = List(FrameworkType)
    databases = List(DatabaseType)
    operating_systems = List(OperatingSystemType)
    services = List(ServiceType)
    tools = List(ToolType)
    user_by_username = Field(UserType, username=String(required=True))

    def resolve_programing_languages(root, info, **kwargs):
        return ProgramingLanguage.objects.all()

    def resolve_frameworks(root, info, **kwargs):
        return Framework.objects.all()

    def resolve_databases(root, info, **kwargs):
        return Database.objects.all()

    def resolve_operating_systems(root, info, **kwargs):
        return OperatingSystem.objects.all()

    def resolve_services(root, info, **kwargs):
        return Service.objects.all()

    def resolve_tools(root, info, **kwargs):
        return Tool.objects.all()

    def resolve_user_by_username(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None


schema = Schema(query=Query)
