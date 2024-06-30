
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HomePageBackground(models.Model):
    title = models.CharField(max_length=255)
    background_image = models.ImageField()

    def __str__(self):
        return self.title


class Services(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_count = models.IntegerField()
    def __str__(self):
        return self.name

class CaruselImages(models.Model):
    image = models.ImageField()



class ReklomCard(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title