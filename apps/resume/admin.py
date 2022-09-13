from django.contrib import admin
from .models import ResumeModel, Advantage, Skill, Service, Project, FeedBack
# Register your models here.

admin.site.register(ResumeModel)
admin.site.register(Advantage)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(FeedBack)