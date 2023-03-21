from django.db import models

class design(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class examination(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class poc(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class install(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class comissioning(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class accept(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class migration(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class other_jobs(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class subcontractor(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class other(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class unenxpected(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class business_trip(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)

class rates(models.Model):
    name = models.CharField(max_length=255, null=True)
    days_architect = models.IntegerField(null=True)
    days_engineer = models.IntegerField(null=True)
    days_manager = models.IntegerField(null=True)
    days_tech_writer = models.IntegerField(null=True)