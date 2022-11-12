from django.db import models

# Create your models here.
class Task(models.Model):
    subject = models.CharField(max_length=150)
    descripcion= models.CharField(max_length=250)

    def __str__ (self):
        return self.subject