from django.urls.base import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Article 
from django.contrib.auth.mixins import (LoginRequiredMixin,
UserPassesTestMixin
)
# Create your views here.
class ArticleListView(ListView):
    model = Article 
    template_name = 'article_list.html'
class ArticleDetailView(DetailView):
    model = Article 
    template_name = 'article_detail.html'
class ArticleUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = Article 
    fields = ('title','body',)
    template_name = 'article_edit.html'
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user  
class ArticleDeleteView(DeleteView,LoginRequiredMixin,UserPassesTestMixin):
    model = Article 
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 
class ArticleCreateView(CreateView,LoginRequiredMixin):
    model = Article 
    template_name = 'article_create.html'
    fields = ('title','body',)
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)