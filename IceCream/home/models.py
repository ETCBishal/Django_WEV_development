from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name