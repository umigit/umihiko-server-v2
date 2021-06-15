import graphene
from graphene_django import DjangoObjectType
from app.models import Tool


class ToolType(DjangoObjectType):
    class Meta:
        model = Tool
        fields = ("name", "experience_period", "skilled", "like")


class Query(graphene.ObjectType):
    all_tools = graphene.List(ToolType)
    tool_by_name = graphene.Field(ToolType, name=graphene.String(required=True))


schema = graphene.Schema(query=Query)
