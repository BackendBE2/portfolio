from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ResumeModel, Advantage, Skill, Service, Project, FeedBack
from apps.blog.models import Blog
from apps.contact.forms import ContactForm


# Create your views here.

def resume_view(request):
    cv = ResumeModel.objects.all().last()
    object_advantages = Advantage.objects.all()
    object_skills = Skill.objects.all()
    object_service = Service.objects.all()
    object_projects = Project.objects.all()
    object_feedbacks = FeedBack.objects.all()
    blog_list = Blog.objects.all()

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'{obj.subject} xabaringiz muvofaqyatli jo\'natildi')
            return redirect('/#contact-sections')
    context = {"cv": cv, "object_advantages": object_advantages, "object_skills": object_skills,
               "object_service": object_service, "object_projects": object_projects,
               "object_feedbacks": object_feedbacks, "blog_list": blog_list, "form": form,
               }
    return render(request, 'index.html', context)
