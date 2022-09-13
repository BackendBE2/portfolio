from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=221)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
