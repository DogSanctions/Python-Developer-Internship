from django.shortcuts import render, get_list_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import User
from .models import Pet
from .models import Post
from .forms import UserForm
from .forms import PostForm
from .forms import PetForm


def perfectwalk_home(request):
    return render(request, 'PerfectWalk/perfectwalk_home.html', {})


def index(request):
    get_posts = Post.Posts.all()
    context = {'posts': get_posts}
    return render(request, 'PerfectWalk/perfectwalk_index.html', context)


def create_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PWindex')
    else:
        print(form.errors)
        form = UserForm()
    return render(request, 'PerfectWalk/perfectwalk_create.html', {'form': form})


def create_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PWindex')
    else:
        print(form.errors)
        form = PetForm()
    return render(request, 'PerfectWalk/perfectwalk_create.html', {'form': form})


def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PWindex')
    else:
        print(form.errors)
        form = PostForm()
    return render(request, 'PerfectWalk/perfectwalk_create.html', {'form': form})


def perfectwalk_details(request, pk):
    get_posts = get_object_or_404(Post, pk=pk)
    context = {'posts': get_posts}
    return render(request, 'PerfectWalk/perfectwalk_details.html', context)


def perfectwalk_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.post_time = timezone.now()
            post.save()
            return redirect('PWpostDetails', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'PerfectWalk/perfectwalk_edit.html', {'form': form, 'pk': pk})


def perfectwalk_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('PWindex')
    return render(request, 'PerfectWalk/perfectwalk_delete.html', {'posts': post})
