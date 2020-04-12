from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from account.views import User
from .forms import CommentForm
from django.contrib import messages as msg
from django import forms

# Create your views here.
def blogs(request):

    blogs = blog.objects.order_by('-id')
    content = {
        'posts' : blogs
    }
    return render(request, 'blog.html', content)

def detailed(request, id):
    post = get_object_or_404(blog, id=id)
    form = CommentForm(request.POST or None)
    latestBlog = blog.objects.order_by('-id')
    if request.method == 'POST':
        if form.is_valid():
            form.instance.name = request.user.first_name +' ' + request.user.last_name
            form.instance.post = post
            form.save()
            return redirect('.', kwargs={
                'id': post.id
            })
    content = {
        'form':form,
        'post': post,
        'latestBlogs':latestBlog,
    }

    return render(request, 'blog-single.html', content)