from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notice_images/', blank=True, null=True)  # For photos
    document = models.FileField(upload_to='notice_docs/', blank=True, null=True)  # For documents

    def __str__(self):
        return self.title