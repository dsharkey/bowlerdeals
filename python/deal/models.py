from django.db import models
import datetime

# Create your models here.

class Deal(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    
    # image_name = models.CharField(max_length=512)

    start_date = models.DateTimeField(default=datetime.datetime.utcnow, db_index=True)
    end_date = models.DateTimeField(db_index=True)
    
    start_price = models.DecimalField(max_digits=6, decimal_places=2)
    current_price =  models.DecimalField(max_digits=6, decimal_places=2)
