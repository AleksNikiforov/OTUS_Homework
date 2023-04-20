from django.db import models



class Rates(models.Model):
    person = models.CharField(max_length=200)
    engineer_cost = models.FloatField(null=False)
    architect_cost = models.FloatField(null=False)
    tech_pisatel_cost = models.FloatField(null=False)
    tech_pisatel_coef = models.FloatField(null=False)
    tech_pisatel_coef = models.FloatField(null=False)

    def __str__(self):
        return self.person