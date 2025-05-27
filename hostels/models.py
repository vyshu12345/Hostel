from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='hostel_images/', null=True, blank=True)


    def __str__(self):
        return self.name
