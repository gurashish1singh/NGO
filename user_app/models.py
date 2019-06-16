from django.db import models


class UserProfile(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    CMA = models.IntegerField()
    Phone = models.DecimalField(max_digits=10, decimal_places=0)
    Email = models.EmailField()
    Address1 = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=10)
    Country = models.CharField(max_length=20)
    Urbanization = models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name, self.Last_Name
