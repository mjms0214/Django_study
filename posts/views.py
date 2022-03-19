from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    
    return render(request, template_name = 'list.html', context = ctx)


def post_detail(request, pk):
    post = Post.objects.get(id = pk)
    ctx = {'post': post}
    
    return render(request, template_name = 'detail.html', context= ctx)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    
    else:
        form = PostForm()
        
    return render(request, 'create.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('posts:list')


def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            return redirect('posts:detail', pk)
    else :
        form = PostForm(instance = post)
        ctx = {'form' : form}

        return render(request, template_name = 'create.html', context = ctx)
    