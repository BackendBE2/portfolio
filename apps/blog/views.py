from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import Blog, Tag, Category
from apps.comment.models import CommentModel

# Create your views here.
from apps.comment.forms import CommentForm


def blog_views(request):
    blog_list = Blog.objects.all()

    q = request.GET.get("q")
    if q:
        blog_list = Blog.objects.filter(title__icontains=q)

    tag = request.GET.get("tag")
    if tag:
        blog_list = Blog.objects.filter(tags__title__exact=tag)

    category = request.GET.get("category")
    if category:
        blog_list = Blog.objects.filter(category__title__exact=category)

    page_number = request.GET.get("page")
    p = Paginator(blog_list, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context = {"blog_list": blog_list, "page_obj": page_obj}
    return render(request, 'blog.html', context)


def views_up(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.views += 1
    blog.save()
    return redirect("blog:blog-single", blog.pk)


def blog_single(request, pk):
    blog_obj = Blog.objects.get(id=pk)
    recent_articles = Blog.objects.all().order_by("-created_at")[:3]
    categories = Category.objects.all()
    for category in categories:
        category.n = len(Blog.objects.filter(category=category))
    tags = Tag.objects.all()

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.blog = blog_obj
            obj.save()
            return redirect('.')

    context = {"blog_obj": blog_obj, "tags": tags, "form": form,
               "recent_articles": recent_articles,
               "categories": categories}
    return render(request, 'single.html', context)
