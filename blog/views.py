from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import (Post, Comment, Category)


class PostListView(View):
    template_name = 'blog/blog_list.html'
    queryset = Post.objects.all()
    latest_post = Post.objects.latest('created_on')

    def get_queryset(self):
        return self.queryset

    def get_latest_post(self):
        return self.latest_post

    def get(self, request, *args, **kwargs):
        context = {
            'posts': self.get_queryset(),
            'latestpost': self.get_latest_post()
        }
        return render(request, self.template_name, context)


class PostObjectMixin(object):
    model = Post

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = None
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
        return obj


class PostDetailView(PostObjectMixin, View):
    template_name = 'blog/blog_detail'

    def get(self, request, pk=None, *args, **kwargs):
        # GET METHOD
        context = {'post': self.get_object()}
        if pk is not None:
            obj = get_object_or_404(Post, pk=pk)
            context['object'] = obj
        return render(request, self.template_name, context)


