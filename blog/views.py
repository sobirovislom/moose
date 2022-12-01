import email
from email import contentmanager
from django.shortcuts import render, HttpResponse
from .models import Post, Contact, About, Comment, Subscribe
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-views')[:4]
    if request.method == 'POST':
        email_subscribe = request.POST.get('email')
        obj = Subscribe.objects.create(email=email_subscribe)
        obj.save()

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def about(request):

    abouts = About.objects.all().filter(is_visible=True)
    context = {
        'abouts' : abouts
    }
    return render(request, "about.html", context=context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        obj = Contact.objects.create(name=name, subject=subject, message=message, email=email)
        obj.save()
    return render(request, "contact.html")


def blog(request):
    page_number = request.GET.get('page')
    if page_number is None:
        page_number = 1
    posts = Post.objects.filter(is_published=True).order_by('views') [:4]
    p = Paginator(posts, 2)
    objs = p.get_page(page_number)
    context = {
        "posts": objs

    }
    return render(request, "blog.html", context=context)
    

def blog_single(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        msg = request.POST.get('msg')
        obj = Comment.objects.create(name=name, email=email, website=website, message=msg, post_id=pk)
        obj.save()
    comments = Comment.objects.filter(post_id=pk)
    post = Post.objects.get(id=pk)
    post.views += 1
    post.save()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, "blog-single.html", context=context)



