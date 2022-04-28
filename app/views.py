"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import PoolForm
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from .models import Blog
from .forms import BlogForm

from .models import Comment
from .forms import CommentForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Наши контакты.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас.',
            'year':datetime.now().year,
        }
    )

def exclusive(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/exclusive.html',
        {
            'title':'Ссылки',
            'message':'Сведения.',
            'year':datetime.now().year,
        }
    )


def pool(request):
    assert isinstance(request, HttpRequest)
    data = None
    
    if request.method == "POST":
        form = PoolForm(request.POST)
        assert isinstance(request,HttpRequest)
        data = None
        if form.is_valid():
            data = dict()
            #name = request.POST['name']
            data['name'] = form.cleaned_data['name']
            #msg = request.POST['msg']
            data['product'] = form.cleaned_data['product']
            data['message'] = form.cleaned_data['message']
            data['score'] = form.cleaned_data['score']
            if (form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            #data['msg'] = form.cleaned_data['msg']
            form = None
    else:
        form = PoolForm()
    return render(
        request,
        'app/pool.html',
        {
            'form':form,
            'data':data
        }
    )

def registration(request):
    """Renders the registratipn page."""

    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()

            return redirect('home')
    else:
        regform = UserCreationForm()
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform,

            'year':datetime.now().year,
        }
    )

def blog(request):
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':"Блог",
            'posts':posts,
            'year':datetime.now().year,
        }
    )

def blogpost(request,parametr):

    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Blog.objects.get(id=parametr)
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
            form = CommentForm()

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,

            'comments': comments,
            'form': form,

            'year':datetime.now().year,
        }
    )



def newpost(request):
    assert isinstance(request,HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            return redirect('blog')
    else:
        blogform = BlogForm()


    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',
            'year':datetime.now().year,
        }

    )

def videopost(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'year':datetime.now().year,
        }
    )
    
