from django.db import models

# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=221)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name