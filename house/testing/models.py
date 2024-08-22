from django.db import models

# Create your models here.
class Myblog(models.Model):
    title =models.CharField(max_length=40)
    author =models.CharField(max_length=30, null=True, blank=True)
    content =models.TextField(blank=True,null=True)
    # slug =models.SlugField(unique=True)
    created =models.DateField(auto_now_add=True)
    # image =models.ImageField(upload_to='images')

    def __str__(self):
        return self.title