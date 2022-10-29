from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=29)
    mobile=models.IntegerField()
    loc=models.CharField(max_length=20)

    def __str__(self):
        return self.name
