from django.db import models

# Create your models here.
class Center(models.Model):
    ide=models.IntegerField()
    name=models.CharField(max_length=100,default="None")
    address=models.CharField(max_length=100,default="None")
    district=models.CharField(max_length=100,default="None")
    test_type=models.CharField(max_length=100,default="None")
    lab_type=models.CharField(max_length=100,default="None")
    latitude=models.DecimalField(max_digits=9,decimal_places=6,default=1.00000)
    longitude=models.DecimalField(max_digits=9,decimal_places=6,default=1.0000)
    def __str__(self):
        return self.name
        class Meta:
            ordering=['district']