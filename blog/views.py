from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView,
                                  DeleteView
                                  )
                                  
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)

        ctx['title'] = 'Main page'
        
        return ctx

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user-news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['title'] = f'{self.kwargs.get("username")}\'s posts'

        return ctx
    


class NewsDetailView(DetailView):
    model = News
    
    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)

        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)

        ctx['title'] = 'Article update'
        ctx['btn_title'] = 'Article update'
        
        return ctx

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = 'home'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        return False
    

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main page'
    }

    return render(request, 'blog/home.html', data)

def about(request):
    return render(request, 'blog/about.html')

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Page with contacts'})







# Create your views here.
