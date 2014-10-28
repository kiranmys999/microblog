# Create your views here.
from .models import Post
## from django.shortcuts import render
from django.views.generic import ListView, DetailView

'''
def blog_list(request, *args, **kwargs):
  post_list = Post.objects.filter(published=True)
  template_name = "blog/post_list.html"
  
  context = {"post_list" : post_list}
  
  return render(request, template_name, context)
'''

'''
def blog_detail(request, pk, *args, **kwargs):
  post = Post.objects.get(pk=pk, published=True)
  template_name = "blog/post_detail.html"
  
  context = {'post' : post}
  
  return render(request, template_name, context)
'''

class PublishedPostMixin(object):
  def get_queryset(self):
    queryset = super(PublishedPostMixin, self).get_queryset()
    return queryset.filter(published=True)

class PostListView(PublishedPostMixin, ListView):
  model = Post
  '''
  def get_queryset(self):
    queryset = super(PostListView, self).get_queryset()
    return queryset.filter(published=True)
  '''
  
class PostDetailView(PublishedPostMixin, DetailView):
  model = Post
  '''
  def get_queryset(self):
    queryset = super(PostDetailView, self).get_queryset()
    return queryset.filter(published=True)
  '''