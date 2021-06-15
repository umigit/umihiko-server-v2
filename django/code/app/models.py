from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=200, null=False)
    experience_period = models.CharField(max_length=200)
    skilled = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
