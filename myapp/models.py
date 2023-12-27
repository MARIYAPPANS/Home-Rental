from django.db import models


class usermodel(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255, default='123')

    def __str__(self):
        return self.email
class House(models.Model):
    owner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    cost_of_rent = models.DecimalField(max_digits=10, decimal_places=2)
    restrictions = models.TextField()
    bedrooms = models.IntegerField()
    ac_non_ac = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='house_photos/')  
    def __str__(self):
      return self.owner_name