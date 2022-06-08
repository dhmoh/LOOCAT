from django.db import models
from retail.models import product
from datetime import datetime
# Create your models here.
class Enter(models.Model):
    user = models.CharField(max_length=60)
    enter_date = models.DateTimeField(auto_now_add=True)
    is_enter = models.BooleanField(default=True)
    detect_id = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.user

class PAYMENT(models.Model):
    user = models.CharField(max_length=60)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quant = models.IntegerField()
    date_time = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.user
