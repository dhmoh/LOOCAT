from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=1000)
    k_name = models.CharField(max_length=20)
    quant = models.IntegerField(default=3)
    info = models.TextField(null=True)
    is_active = models.BooleanField(default=True)




