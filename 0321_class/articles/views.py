from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save() 
        # title =	request.POST.get('title')	
        # content = request.POST.get('content')
        # article = Article(title=title,	content=content)
        # article.save()
            return redirect('articles:detail',article.pk)
        # return redirect('articles:create')
    
    else: # (or elif request.method == 'GET':)
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html',context)

# def new(request):
#     return render(request, 'articles/new.html')

def update(request,pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html',context)

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article':article,
#     }
#     return render(request, 'articles/edit.html',context)

def detail(request,pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html',context)

def delete(request,pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        redirect('articles:detail', article.pk)