from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class HomePageView(TemplateView):
    template_name="index.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class PostListView(LoginRequiredMixin, ListView):
    model=Post
    template_name="post_list.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model= Post
    template_name ="post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name="post_new.html"
    fields=['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=['title', 'body']

    def test_func(self):
        obj=self.get_object()
        return obj.author.id == self.request.user.id


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url=reverse_lazy("post_list")

    def test_func(self):
        obj=self.get_object()
        return obj.author.id == self.request.user.id

