from django.db import models

# Create your models here.

## Basic models for blog post, author, category, and the blog post itself
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    # This is the author's profile picture
    profile_picture = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    # This has to be named category, not categories
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
