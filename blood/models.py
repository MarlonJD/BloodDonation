from django.db import models
from django.contrib.auth.models import User


class blood_donor(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=200)
    last_donation = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Name: {} message {}".format(self.name, self.message)

    class Meta:
        ordering = ['-date']
