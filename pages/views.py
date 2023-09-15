from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'all_posts_list'


class BlogDetailView(DetailView): 
    model = Post
    template_name = 'pages/post_detail.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'pages/post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'pages/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): 
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')




