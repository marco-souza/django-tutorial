from django.db import models


# Create your models here.
class Pet(models.Model):
    specie = models.CharField(max_length=20)
    name = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.specie


class Photo(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=120)
    img_base64 = models.CharField(max_length=1000)

    def __str__(self):
        return self.img_url


class Coordinate(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{}lat x {}long".format(
            self.latitude,
            self.longitude,
        )
