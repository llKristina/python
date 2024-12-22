from django.db import models

class Galaxy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    distance_from_earth = models.FloatField(help_text="Distance in light years")

    def __str__(self):
        return self.name

class Star(models.Model):
    name = models.CharField(max_length=100)
    galaxy = models.ForeignKey(Galaxy, on_delete=models.CASCADE, related_name="stars")
    mass = models.FloatField(help_text="Mass in solar masses")
    brightness = models.FloatField(help_text="Brightness in solar units")

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=100)
    star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name="planets")
    has_life = models.BooleanField(default=False)

    def __str__(self):
        return self.name
