"""create your views here"""
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import BlogPost, Profile
from .forms import BlogPostForm, SignUpForm


def post_list(request):
    """post_list"""
    list = BlogPost.objects.all().order_by('-created_date')
    paginator = Paginator(list, 5)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'blog_app/post_list.html', {'posts': post})


def myblogs(request):
    """my blogs view"""
    post = BlogPost.objects.filter(author=request.user).order_by('-created_date')
    paginator = Paginator(post, 5)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'blog_app/random_string.html', {'posts': post})


def create_post(request):
    """create post"""
    form = BlogPostForm(request.POST or None, author=request.user)
    if form.is_valid():
        # form.author = render.user
        form.save()
        return redirect('my_blog')
    return render(request, 'blog_app/blogpost_form.html', {'form': form})


def update_post(request, id):
    """ update post view"""
    post = BlogPost.objects.get(pk=id)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('my_blog')
    return render(request, 'blog_app/blogpost_form.html', {'form': form, 'post': post})


def delete_post(request, id):
    """delete view"""
    post = BlogPost.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('my_blog')
    return render(request, 'blog_app/blogpost_confirm_delete.html', {'post': post})


class PostDetailView(DetailView):
    """ post details view"""
    model = BlogPost


def signup(request):
    """sign up view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user, user_profile = form.save(commit=False)
        if form.is_valid():
            # username = user.cleaned_data.get('username')
            # raw_password = user.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = SignUpForm
    return render(request, 'blog_app/signup.html', {'form': form})


def userprofiledetails(request):
    """user profile view"""
    user_profile = Profile.objects.filter(user=request.user)
    post = BlogPost.objects.filter(author=request.user).order_by('-created_date')
    return render(request, 'blog_app/my_profile.html', {'posts': post,
                                                        'user_profile': user_profile})
