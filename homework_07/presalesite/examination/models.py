from django.db import models


class Examination(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)