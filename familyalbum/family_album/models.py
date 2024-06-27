from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE, related_name='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.id}"
