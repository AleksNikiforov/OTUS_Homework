from django.db import models



class Rates(models.Model):
    name = models.CharField(max_length=200)
    days = models.FloatField(null=True)
    
    def __str__(self):
        return self.name