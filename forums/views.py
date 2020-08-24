from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse


def forums(request):
    return render(request,'forums/forum.html',{})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def PostDetail(request, pk):
    post = Post.objects.get(id=pk)
    content = {
        'post':post,
        'comments':Comment.objects.filter(post=post)
    }
    return render(request,'forums/post_detail.html',content)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title','short_description','content']

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    form_class=PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.writer:
            return True
        else: return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/forums'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.writer:
            return True
        else: return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.post = Post.objects.get(id = self.kwargs['pk'])
        
        form.instance.user = self.request.user
        return super().form_valid(form)

def delete_comment(request, **kwargs):
    comment = Comment.objects.get(id=kwargs['id'])
    post = Post.objects.get(id=kwargs['pk'])
    content = {
        'post':post,
        'comments':Comment.objects.filter(post=post)
    }
    if request.user.username == comment.user.username:
        comment.delete()
    return render(request,'forums/post_detail.html',content)
    