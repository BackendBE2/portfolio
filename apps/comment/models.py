from django.db import models
from apps.blog.models import Blog
# Create your models here.


class CommentModel(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='comment', null=True, blank=True)
    email = models.EmailField()
    website = models.CharField(max_length=221)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
