from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.

def home(request):
    posts=Post.objects.all().order_by('-published_date')
    return render(request,'blogApp/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blogApp/post_detail.html',{'post':post})

def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid:
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blogApp/post_edit.html',{'form':form})

def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid:
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,'blogApp/post_edit.html',{'form':form})

def post_remove(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home')

def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form=CommentForm()
    return render(request,'blogApp/add_comment.html',{'form':form})

