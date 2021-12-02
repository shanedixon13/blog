from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class HomePageView(TemplateView):
    template_name="index.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class PostListView(ListView):
    model=Post
    template_name="post_list.html"


class PostDetailView(DetailView):
    model= Post
    template_name ="post_detail.html"


class PostCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields=['title', 'body', 'author']


class PostEditView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=['title', 'body']


class PostDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url=reverse_lazy("post_list")

