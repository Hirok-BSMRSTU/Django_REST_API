from django.db import models

# Create your models here.
class Contract(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
