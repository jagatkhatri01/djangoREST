from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.city
class Person(models.Model):
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE, related_name="people")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

