from django.db import models

class Design(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)


class Poc(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Install(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Comissioning(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Accept(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Migration(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Other_jobs(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Subcontractor(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Other(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Unenxpected(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Business_trip(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class Rates(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)