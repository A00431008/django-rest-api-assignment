from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name