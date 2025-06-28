from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='state_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TouristPlace(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='place_images/', blank=True, null=True)
    best_time = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    main_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def location_url(self):
        if self.location:
            return f"https://www.google.com/maps/search/?api=1&query={self.location.replace(' ', '+')}"
        return "#"

class PlaceImage(models.Model):
    place = models.ForeignKey(TouristPlace, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='place_images/')

    def __str__(self):
        return f"Image for {self.place.name}"
