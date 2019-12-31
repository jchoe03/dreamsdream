from django.db import models

# Create your models here.
class School(models.Model):
    title = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True) #돈은 안쪽에 보이게
    duration = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)
    donors = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title





