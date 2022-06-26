from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_confirm_delete.html"