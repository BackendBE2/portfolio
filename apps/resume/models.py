from django.db import models


class ResumeModel(models.Model):
    title = models.CharField(max_length=221)
    resume = models.FileField(upload_to='resume/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=221)
    icon = models.FileField(upload_to='icons/')
    count = models.IntegerField()

    def  __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=221)
    percentage = models.IntegerField()
    last_week = models.IntegerField()
    last_month = models.IntegerField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=221)
    icon = models.FileField(upload_to='icons/')
    content = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=221)
    direction = models.CharField(max_length=221)
    url = models.URLField()

    def  __str__(self):
        return self.title


class FeedBack(models.Model):
    avatar = models.ImageField(upload_to='feedbacks/')
    name = models.CharField(max_length=221)
    position = models.CharField(max_length=221)
    feedback = models.TextField()

    def __str__(self):
        return self.name


