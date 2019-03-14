from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

def posts_list(request, *args, **kwargs):
    articles = Article.objects.all()
    return render(request, 'blog_posts/blog_posts.html',{'articles':articles})

def post_new(request, *args, **kwargs):
    form = ArticleForm()
    return render(request,'blog_posts/post_article.html' ,{'form': form})

def login(request, *args, **kwargs):
    pass
