from django.db import models
from django.utils import timezone

class Product(models.Model):
    #author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=50,decimal_places=2)
    price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
                                                             
        
     
    
def publish(self):
    self.updated_at = timezone.now()
    self.save()

def __str__(self):
    return self.title
